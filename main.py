#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
import sys;
from math import inf;
from typing import Callable;
from typing import List;
from yaml import load;
from yaml import FullLoader;

from problems.day1 import main as day1;
from problems.day2 import main as day2;
from problems.day3 import main as day3;
from problems.day4 import main as day4;
from problems.day5 import main as day5;
from problems.day6 import main as day6;
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

FILE_CONFIG     = 'config.yml';
FILE_TESTCONFIG = 'testdata/config.yml';

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    ## prüfe cli args:
    args = sys.argv[1:];
    flag       = args[0] if len(args) > 0 else '';
    TESTMODE   = not not re.match(r'^-+test$', flag, re.IGNORECASE);
    if not TESTMODE:
        args = [''] + args;
    index_from = int(args[1]) if len(args) > 1 else 0;
    index_to   = int(args[2]) if len(args) > 2 else inf;
    ## extrahiere Szenarien:
    config = read_config(FILE_TESTCONFIG if TESTMODE else FILE_CONFIG);
    ## Szenarien laufen lassen:
    for case in config['cases'] or []:
        index = case['index'];
        if index < index_from or index > index_to:
            continue;
        content         = case['content'] if 'content' in case else None;
        path            = case['path'] if 'path' in case else None;
        remove_comments = case['remove_comments'];
        if isinstance(content, str):
            lines = process_content(re.split(r'\n', content), remove_comments=remove_comments)
        elif isinstance(path, str):
            lines = read_file(path=path, remove_comments=remove_comments);
        else:
            lines = [];
        title    = case['title'];
        method   = eval(case['method']);
        expected = (case['expected'] or dict(value=None))['value'] if TESTMODE else None;
        params   = case['params'] if 'params' in case else {};
        call_method(title=title, f=method, lines=lines, testmode=TESTMODE, expected=expected, **params);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def call_method(title: str, f: Callable, lines: List[str], **kwargs):
    print('\n[\033[94;1mINFO\033[0m] {}'.format(title));
    f(lines, **kwargs);
    print('');
    return;

def read_file(path: str, remove_comments: bool = True) -> List[str]:
    lines = [];
    with open(path, mode='r') as fp:
        lines = fp.readlines();
    lines = process_content(lines, remove_comments=remove_comments);
    return lines;

def process_content(lines: List[str], remove_comments: bool = True) -> List[str]:
    # remove spaces at the beginning and end:
    lines = [_.strip() for _ in lines];
    # (optional) remove lines which are just comments:
    if remove_comments:
        lines = [_ for _ in lines if not re.match(r'^\s*#', _)];
    return lines;

def read_config(path: str) -> dict:
    with open(path, 'r') as fp:
        spec = load(fp, Loader=FullLoader);
        if not isinstance(spec, dict):
            raise ValueError('Config is not a dictionary object!');
        return spec;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXECUTION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main();
