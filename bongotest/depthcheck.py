from itertools import groupby
from operator import itemgetter


def print_depth(data):
    depths = sorted(get_depths(data), key=lambda tup: tup[1])
    keys_grouped_by_depth = [(key, list(list(zip(*group))[0])) for key, group in groupby(depths, itemgetter(1))]
    print_keys_grouped_by_depth(keys_grouped_by_depth)


def print_keys_grouped_by_depth(keys_grouped_by_depth):
    for depth, keys in keys_grouped_by_depth:
        for key in sorted(keys):
            print '{}: {}'.format(key, depth)


def get_depths(data, curr_depth=0):
    """
    Finds least common ancestor for given two nodes
    Args:
        data (dict): A dictionary object containing key value pairs
        curr_depth (int): Initial depth for the current level of the data dict
    Returns:
        list: A list of tuple of form (key, depth) for each key in the given dict
    """
    depths = []
    for k in data:
        depths.append((k, curr_depth + 1))
        if type(data[k]) is dict:
            depths.extend(get_depths(data[k], curr_depth + 1))
        if hasattr(data[k], '__dict__'):
            depths.extend(get_depths(data[k].__dict__, curr_depth + 1))

    return depths
