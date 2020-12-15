#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
from numpy import asarray;
from typing import List;
from typing import Tuple;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], oldpolicy: bool, **kwargs):
    values = extract_data(lines);
    solutions = check_validity(values, oldpolicy);
    display_solutions(solutions);
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
        i = int(m.group(1));
        j = int(m.group(2));
        a  = m.group(3);
        w  = re.split(r'', m.group(4));
        values.append((i, j, a, w));
    return values;

def check_validity(values: List[Tuple[int,int,str,List[str]]], oldpolicy: bool) -> List[bool]:
    n = len(values);
    if oldpolicy:
        freq = [len([u for u in w if u == a]) for _, _, a, w in values];
        solutions = [values[k][0] <= freq[k] and freq[k] <= values[k][1] for k in range(n)];
    else:
        letterOne = asarray([(1*(w[i] == a) if i < len(w) else 0) for i, _, a, w in values]);
        letterTwo = asarray([(1*(w[j] == a) if j < len(w) else 0) for _, j, a, w in values]);
        solutions = ((letterOne + letterTwo) % 2 == 1).tolist();
    return solutions;

def display_solutions(solutions: List[bool]):
    n = len(solutions);
    n_correct = sum(solutions);
    print('  Es gab \033[92;1m{n}\033[0m Fälle:\n  - \033[4;1m{correct}\033[0m korrekt\n  - \033[4;1m{incorrect}\033[0m inkorrekt'.format(
        n=n,
        correct=n_correct,
        incorrect=n-n_correct
    ));
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
