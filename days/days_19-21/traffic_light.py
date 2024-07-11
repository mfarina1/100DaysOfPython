import itertools
import sys
import time
import random

colors = 'red green yellow'.split()
colors_it = iter(colors)
light = itertools.cycle(colors_it)

def random_timer():
    return random.randint(2, 6)

def traffic_light(rotation):
    """
    Use itertools to create a script that simulates traffic lights!

    The idea is to perhaps... cycle (hint hint!) through the different colours of a set of traffic lights 
    - red, amber and green - printing the name of the colour every time the cycle occurs.

    For bonus points: traffic lights normally cycle between green and red based on traffic levels,
    so you never know exactly when the change will happen.
    This is a great chance to throw some randomness into your script.
    """

    for color in rotation:
        if color == 'yellow':
            print('Caution! The light is %s' % color)
            time.sleep(3)
            
        elif color == 'red':
            print("Stop! the light is %s" % color)
            time.sleep(random_timer())

        else:
            print("Go! The light is %s" % color)
            time.sleep(random_timer())

    """
    tend = time.time() + seconds
    while time.time() < tend:
        # '\r' is carriage return: return cursor to the start of the line.
        sys.stdout.write('\r' + next(light) + '\n')  # no newline
        sys.stdout.flush()
        time.sleep(2.0)
    print()"""


if __name__ == "__main__":
    traffic_light(light)