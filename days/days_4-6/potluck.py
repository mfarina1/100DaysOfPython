from collections import defaultdict, namedtuple, Counter
import pprint

def potluck():
    # define a named tuple for quantity of each food item at potluck
    FoodItems = namedtuple('FoodItems', ['food', 'quantity'])

    # if someone isn't bringing enough of a food item, we throw an error

    # then create a list of tuples to populate a default(dict) for every person/food at the potluck,
    # using a default dict to allow for multiple food items (values) for each person (key)
    person_and_food = [('Madeline', 'brownies'), ('Nick', 'mac n cheese'), ('Alejandro', 'ribs'),
                    ('Michael', 'salad'), ('Vikas', 'fried rice'), ('Nick', 'watermelon'), ('Madeline', 'cookies')]

    print("Potluck attendees & food: \n")
    pprint.pprint(person_and_food)

    potluck_food = defaultdict(list)
    for name, food in person_and_food:
        potluck_food[name].append(food)

    print("Potluck_food: \n")
    pprint.pprint(potluck_food)

    # then we use a counter to check who's bringing the most food items
    count = Counter()
    for person, food in potluck_food.items():
        count[person] += len(food)

    print("\n Who's bring the most food items? \n")
    print(count.most_common(2))

potluck()