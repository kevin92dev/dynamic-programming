#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from datetime import datetime

start_time = datetime.now()
ordered_list = range(1, 1000000)


def search(seek_element):
    start_index = 0
    end_index = len(ordered_list) - 1

    while start_index <= end_index:
        # Get the middle index
        middle_index = int(start_index + ((end_index - start_index) / 2))

        # If we've found the element just return its position.
        if ordered_list[middle_index] == seek_element:
            return ordered_list[middle_index]

        # Decide which half to choose for seeking next: left or right one.
        if seek_element < ordered_list[middle_index]:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1


print(search(900000))

# Show elapsed time
end_time = datetime.now()
print('\nDuration: {}'.format(end_time - start_time))
