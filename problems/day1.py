#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from itertools import combinations;
from numpy import prod;
from typing import List;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], year: int, tuple_size: int, **kwargs):
    values = extract_data(lines);
    solutions = find_tuples(values, tuple_size, year);
    display_solutions(solutions);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> List[int]:
    values = [];
    for _ in lines:
        try:
            values.append(int(_));
        finally:
            pass;
    return values;

def find_tuples(values: List[int], sz: int, year: int) -> List[List[int]]:
    n = len(values);
    solutions = [list(_) for _ in combinations(values, r=sz) if sum(_) == year];
    return solutions;

def display_solutions(solutions: List[List[int]]):
    print('  Es gibt \033[92;1m{}\033[0m Lösung(en):'.format(len(solutions)));
    for x in solutions:
        print('    {sum} = {sum_value} and {prod} = \033[4;1m{prod_value}\033[0m '.format(
            sum        = ' + '.join([str(_) for _ in x]),
            sum_value  = sum(x),
            prod       = ' · '.join([str(_) for _ in x]),
            prod_value = prod(x)
        ));
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
