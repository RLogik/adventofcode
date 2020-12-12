#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
from typing import Callable;
from typing import List;

from problems.day1 import main as day1;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    call_method('Tag 1', day1, 'data/day1.in', year=2020, tuple_size=2);
    call_method('Tag 1*', day1, 'data/day1.in', year=2020, tuple_size=3);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def call_method(title: str, f: Callable, path: str, **kwargs):
    print('\n[\033[94;1mINFO\033[0m] {}'.format(title));
    lines = read_file(path=path, remove_comments=True);
    f(lines, **kwargs);
    print('');
    return;

def read_file(path: str, remove_comments: bool = True) -> List[str]:
    lines = [];
    with open(path, mode='r') as fp:
        lines = fp.readlines();
    # remove spaces at the beginning and end:
    lines = [_.strip() for _ in lines];
    # (optional) remove lines which are just comments:
    if remove_comments:
        lines = [_ for _ in lines if not re.match(r'^\s*#', _)];
    return lines;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXECUTION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main();
