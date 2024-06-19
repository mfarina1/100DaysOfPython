#!python3

from datetime import timedelta, datetime
from time import sleep

class stopwatch:
    #one_second = timedelta(seconds=1)
    time_elapsed = 'time elapsed: {:.0f}h {:>2.0f}m {:>2.0f}s'
    start_time = dict(hours=0, minutes=0, seconds=0)
    start_state = current_state = timedelta(**start_time)

    @classmethod
    def increment(arg):
        arg.current_state += timedelta(seconds=1)
        hours = arg.current_state.seconds // 3600
        minutes = arg.current_state.seconds // 60 % 60
        seconds = arg.current_state.seconds % 60
        return arg.time_elapsed.format(hours, minutes, seconds)

    @classmethod
    def stop(arg):
        arg.current_state = arg.start_state
        print("\n stopping stopwatch :(")

    @classmethod
    def start(arg):
        elapsed_time = arg.time_elapsed.format(0,0,0)
        print("starting stopwatch :D")
        while True:
            try:
                print(elapsed_time, end='\r')
                sleep(1)
                elapsed_time = arg.increment()
            except KeyboardInterrupt:
                arg.stop()
                break

        

"""
class Stopwatch:

    _ONE_SECOND = timedelta(seconds=1)
    _TIME_ELAPSED = 'time elapsed: {:.0f}h {:>2.0f}m {:>2.0f}s'
    _START_TIME = dict(hours=0, minutes=0, seconds=0)
    _START_STATE = _CURRENT_STATE = timedelta(**_START_TIME)


    @classmethod
    def start(cls):
        time_elapsed = cls._TIME_ELAPSED.format(0, 0, 0)
        print('starting stopwatch... (CTRL+C to stop)')
        while True:
            try:
                print(time_elapsed, end='\r')
                sleep(1)
                time_elapsed = cls._increment()
            except KeyboardInterrupt:
                cls._stop()
                break
    @classmethod
    def _stop(cls):
        cls._CURRENT_STATE = cls._START_STATE
        print('\nstopping stopwatch...')

    @classmethod
    def _increment(cls):
        cls._CURRENT_STATE += cls._ONE_SECOND
        hours = cls._CURRENT_STATE.seconds // 3600
        minutes = (cls._CURRENT_STATE.seconds // 60) % 60
        seconds = cls._CURRENT_STATE.seconds % 60
        return cls._TIME_ELAPSED.format(hours, minutes, seconds)
"""
stopwatch.start()