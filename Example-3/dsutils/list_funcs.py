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