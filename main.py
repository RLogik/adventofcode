#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
from typing import Callable;
from typing import List;
from yaml import load;
from yaml import FullLoader;

from problems.day1 import main as day1;
from problems.day2 import main as day2;
from problems.day3 import main as day3;
from problems.day4 import main as day4;
# from problems.day5 import main as day5;
# from problems.day6 import main as day6;
# from problems.day7 import main as day7;
# from problems.day8 import main as day8;
# from problems.day9 import main as day9;
# from problems.day10 import main as day10;
# from problems.day11 import main as day11;
# from problems.day12 import main as day12;
# from problems.day13 import main as day13;
# from problems.day14 import main as day14;
# from problems.day15 import main as day15;
# from problems.day16 import main as day16;
# from problems.day17 import main as day17;
# from problems.day18 import main as day18;
# from problems.day19 import main as day19;
# from problems.day20 import main as day20;
# from problems.day21 import main as day21;
# from problems.day22 import main as day22;
# from problems.day23 import main as day23;
# from problems.day24 import main as day24;
# from problems.day25 import main as day25;
# from problems.day26 import main as day26;
# from problems.day27 import main as day27;
# from problems.day28 import main as day28;
# from problems.day29 import main as day29;
# from problems.day30 import main as day30;
# from problems.day31 import main as day31;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GLOBAL VARIABLES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TESTMODE    = False;
FILE_CONFIG = 'config.yml';

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    config = read_config();
    for case in config['testcases' if TESTMODE else 'cases'] or []:
        title           = case['title'];
        method          = eval(case['method']);
        path            = case['path'];
        remove_comments = case['remove_comments'];
        expected        = (case['expected'] or dict(value=None))['value'] if TESTMODE else None;
        params          = case['params'] or {};
        call_method(title=title, f=method, path=path, remove_comments=remove_comments, testmode=TESTMODE, expected=expected, **params);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def call_method(title: str, f: Callable, path: str, remove_comments: bool, **kwargs):
    print('\n[\033[94;1mINFO\033[0m] {}'.format(title));
    lines = read_file(path=path, remove_comments=remove_comments);
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

def read_config() -> dict:
    fname = FILE_CONFIG;
    with open(fname, 'r') as fp:
        spec = load(fp, Loader=FullLoader);
        if not isinstance(spec, dict):
            raise ValueError('Config is not a dictionary object!');
        return spec;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXECUTION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main();
