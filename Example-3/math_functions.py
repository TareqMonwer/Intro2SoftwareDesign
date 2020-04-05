"""
LIST FUNCTIONS
"""


def get_max(list):
    mx = float("-inf")
    for n in list:
        if n > mx:
            mx = n
    return mx


def get_min(list):
    mn = float("inf")
    for num in list:
        if num < mn:
            mn = num
    return mn


def get_avg(list):
    return sum(list) / len(list)


"""
DICTIONARY FUNCTIONS
"""


def get_keys(dict):
    return dict.keys()


def get_items(dict):
    return dict.items()


def get_max(dict):
    mx = float("-inf")

    for num in dict.values():
        if num > mx:
            mx = num
        return mx
