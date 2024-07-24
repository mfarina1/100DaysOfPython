import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US - - -'.split()
confirmed = [False, True, True, False, True, "-", "-", "-"]

participants_info = zip(names, locations, confirmed)
rotation = itertools.cycle(participants_info)

def get_attendees():
    for i in range(len(names)):
        print(next(rotation))

if __name__ == '__main__':
    get_attendees()

import itertools