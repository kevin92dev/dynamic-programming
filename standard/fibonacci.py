#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Author: Kevin Murillo Fernández
Email: kevin92dev@gmail.com
Copyright 2018
"""

from datetime import datetime

start_time = datetime.now()


def fibonacci(n):
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n


for i in range(40):
    print(fibonacci(i))

# Show elapsed time
end_time = datetime.now()
print('\nDuration: {}'.format(end_time - start_time))
