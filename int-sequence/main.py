"""
The program should return the first integer positive number absent in the provided sequence

As example: 
in the following list, the output should be 2
items = [1, 3, 20, -2, -14, 10]
"""

from typing import List

def find_absent_item(items: List[int]) -> int:
    ordered_items = sorted(items)
    positive_values = list(filter(lambda e: e > 0, ordered_items))
    if len(positive_values) < 1:
        return 1
    values_range = range(positive_values[0], positive_values[-1])
    for index, item in zip(values_range, positive_values):
        if (item > index):
            return index
    return positive_values[-1] + 1