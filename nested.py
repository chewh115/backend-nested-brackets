#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "chewh115, observed Chris coding w/ Janell assisting, & spoke w/ Rob about it. Also updated with demo!"

import sys

brackets_dict = {'(': ')', '[': ']', '{': '}', '<': '>', '(*': '*)'}


def is_nested(line):
    """Validate a single input line for correct nesting"""
    brackets_stack = []
    count = 0
    while line:
        count += 1
        if len(line) > 1:
            token = line[:2]
            if token not in brackets_dict and token not in brackets_dict.values():
                token = line[0]
        else:
            token = line[0]
        line = line[len(token):]
        if token in brackets_dict:
            brackets_stack.append(token)
        elif token in brackets_dict.values():
            if token == brackets_dict[brackets_stack[-1]]:
                brackets_stack.pop()
            else:
                return "NO {}".format(count)
    if brackets_stack:
        return "NO " + str(count)
    return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open(args[0], 'r') as input_file:
        with open('output.txt', 'w') as output_file:
            for line in input_file:
                output_file.write(is_nested(line) + '\n')


if __name__ == '__main__':
    main(sys.argv[1:])
