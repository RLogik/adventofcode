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

def main(lines: List[str], **kwargs):
    # values = extract_data(lines);
    # solutions = check_validity(values, oldpolicy);
    # display_solutions(solutions);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> list:
    values = [];
    for _ in lines:
        pass;
    return values;

def check_validity(values: list) -> List[bool]:
    solutions = [];
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
