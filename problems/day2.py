#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
from numpy import asarray;
from typing import Any;
from typing import List;
from typing import Tuple;

from problems.checkresult import checkresult;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], testmode: bool, expected: Any, oldpolicy: bool, **kwargs):
    values = extract_data(lines);
    valid = check_validity(values, oldpolicy);
    display_solutions(testmode, expected, valid);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> List[Tuple[int,int,str,List[str]]]:
    values = [];
    for _ in lines:
        pattern = r'^\s*(0|[1-9]\d*)\-(0|[1-9]\d*)\s*(\S):\s*(\S*)\s*$';
        m = re.match(pattern, _);
        if not m:
            continue;
        # NOTE: Indexes müssen um 1 verringert werden, da 1 -> n ~~> 0 -> n-1
        values.append((int(m.group(1)) - 1, int(m.group(2)) - 1, m.group(3), [__ for __ in m.group(4)]));
    return values;

def check_validity(values: List[Tuple[int,int,str,List[str]]], oldpolicy: bool) -> List[bool]:
    n = len(values);
    if oldpolicy:
        freq = [len([u for u in w if u == a]) for _, _, a, w in values];
        valid = [values[k][0] <= freq[k] and freq[k] <= values[k][1] for k in range(n)];
    else:
        letterOne = asarray([(1*(w[i] == a) if i < len(w) else 0) for i, _, a, w in values]);
        letterTwo = asarray([(1*(w[j] == a) if j < len(w) else 0) for _, j, a, w in values]);
        ## gültig <==> genau einer der Buchstaben
        valid = ((letterOne + letterTwo) % 2 == 1).tolist();
    return valid;

def display_solutions(testmode: bool, expected: Any, valid: List[bool]):
    n = len(valid);
    result = sum(valid);
    print('  Es gab \033[92;1m{n}\033[0m Codes und davon sind \033[4;1m{result}\033[0m korrekt.'.format(
        n=n,
        result=result,
    ));
    if testmode:
        checkresult(expected, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
