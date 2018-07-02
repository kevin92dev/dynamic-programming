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
    for index in ordered_list:
        if seek_element == ordered_list[index]:
            return ordered_list[index]


print(search(500000))

# Show elapsed time
end_time = datetime.now()
print('\nDuration: {}'.format(end_time - start_time))
