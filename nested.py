#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "chewh115, observed Chris coding with Janell assisting, and spoke with Rob about it too"

import sys


def is_nested(line):
    """Validate a single input line for correct nesting"""
    brackets_dict = {'(': ')', '[': ']', '{': '}', '<': '>', '(*': '*)'}
    opening_brackets = brackets_dict.keys()
    closing_brackets = brackets_dict.values()
    brackets_stack = []
    count_stack = []
    count = 0
    while line:
        if len(line) > 1:
            token = line[:2]
            if token not in opening_brackets and token not in closing_brackets:
                token = line[0]
        else:
            token = line[0]

        if token in opening_brackets:
            brackets_stack.append(token)
            count_stack.append(count)
        elif token in closing_brackets:
            if token == brackets_dict[brackets_stack[-1]]:
                brackets_stack.pop()
                count_stack.pop()
            else:
                return "NO " + str(count)
        line = line[len(token):]
        count += len(token)
    if brackets_stack:
        return "NO " + str(count_stack[0])
    else:
        return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open(args, 'r') as input_file:
        with open('output.txt', 'w') as output_file:
            for line in input_file:
                output_file.write(is_nested(line) + '\n')


main('input.txt')

if __name__ == '__main__':
    main(sys.argv[1])
