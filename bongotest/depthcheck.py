def print_depth(data):
    pass


def get_depths(data, curr_depth=0):
    depths = []
    for k in data:
        depths.append((k, curr_depth + 1))
        if type(data[k]) is dict:
            depths.extend(get_depths(data[k], curr_depth + 1))
        if hasattr(data[k], '__dict__'):
            depths.extend(get_depths(data[k].__dict__, curr_depth + 1))

    return depths
