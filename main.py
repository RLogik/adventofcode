#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
from typing import Callable;
from typing import List;

from problems.day1 import main as day1;
from problems.day2 import main as day2;
from problems.day3 import main as day3;
# from problems.day4 import main as day4;
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

TESTMODE = False;
DATAPATH = 'data' if not TESTMODE else 'testdata'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    call_method(True,  'Tag 1',   day1,  '{}/day1.in'.format(DATAPATH),  testmode=TESTMODE, expected=514579,             year=2020, tuple_size=2);
    call_method(True,  'Tag 1*',  day1,  '{}/day1.in'.format(DATAPATH),  testmode=TESTMODE, expected=241861950,          year=2020, tuple_size=3);
    call_method(True,  'Tag 2',   day2,  '{}/day2.in'.format(DATAPATH),  testmode=TESTMODE, expected=2,                  oldpolicy=True);
    call_method(True,  'Tag 2*',  day2,  '{}/day2.in'.format(DATAPATH),  testmode=TESTMODE, expected=1,                  oldpolicy=False);
    call_method(False, 'Tag 3',   day3,  '{}/day3.in'.format(DATAPATH),  testmode=TESTMODE, expected=([7], 7),           directions=[(3, 1)], show_path=TESTMODE);
    call_method(False, 'Tag 3*',  day3,  '{}/day3.in'.format(DATAPATH),  testmode=TESTMODE, expected=([2,7,3,4,2], 336), directions=[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)], show_path=False);
    # call_method(False, 'Tag 4',   day4,  '{}/day4.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 4*',  day4,  '{}/day4.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 5',   day5,  '{}/day5.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 5*',  day5,  '{}/day5.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 6',   day6,  '{}/day6.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 6*',  day6,  '{}/day6.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 7',   day7,  '{}/day7.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 7*',  day7,  '{}/day7.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 8',   day8,  '{}/day8.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 8*',  day8,  '{}/day8.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 9',   day9,  '{}/day9.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 9*',  day9,  '{}/day9.in'.format(DATAPATH),  testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 10',  day10, '{}/day10.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 10*', day10, '{}/day10.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 11',  day11, '{}/day11.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 11*', day11, '{}/day11.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 12',  day12, '{}/day12.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 12*', day12, '{}/day12.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 13',  day13, '{}/day13.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 13*', day13, '{}/day13.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 14',  day14, '{}/day14.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 14*', day14, '{}/day14.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 15',  day15, '{}/day15.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 15*', day15, '{}/day15.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 16',  day16, '{}/day16.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 16*', day16, '{}/day16.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 17',  day17, '{}/day17.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 17*', day17, '{}/day17.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 18',  day18, '{}/day18.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 18*', day18, '{}/day18.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 19',  day19, '{}/day19.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 19*', day19, '{}/day19.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 20',  day20, '{}/day20.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 20*', day20, '{}/day20.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 21',  day21, '{}/day21.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 21*', day21, '{}/day21.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 22',  day22, '{}/day22.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 22*', day22, '{}/day22.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 23',  day23, '{}/day23.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 23*', day23, '{}/day23.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 24',  day24, '{}/day24.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 24*', day24, '{}/day24.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 25',  day25, '{}/day25.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 25*', day25, '{}/day25.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 26',  day26, '{}/day26.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 26*', day26, '{}/day26.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 27',  day27, '{}/day27.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 27*', day27, '{}/day27.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 28',  day28, '{}/day28.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 28*', day28, '{}/day28.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 29',  day29, '{}/day29.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 29*', day29, '{}/day29.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 30',  day30, '{}/day30.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 30*', day30, '{}/day30.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 31',  day31, '{}/day31.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    # call_method(False, 'Tag 31*', day31, '{}/day31.in'.format(DATAPATH), testmode=TESTMODE, expected=);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def call_method(remove_comments: bool, title: str, f: Callable, path: str, **kwargs):
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXECUTION
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main();
