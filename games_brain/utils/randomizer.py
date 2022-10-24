from random import randint, choice


def get_rand_int(range_to: int):
    '''Returns a random value from 1 to the specified range'''
    return randint(1, range_to)


def get_rand_char(_list):
    ''''Returns a random item from the list'''
    return choice(_list)
