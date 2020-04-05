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