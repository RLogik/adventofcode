#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from math import ceil;
from math import prod;
from numpy import asarray;
from numpy import ndarray;
from numpy import transpose;
from typing import Any;
from typing import List;
from typing import Tuple;

from problems.checkresult import checkresult;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# GLOBAL VARIABLES
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TREESYMBOL        = '#';
NOTREESYMBOL      = '.';
COLLISIONSYMBOL   = 'X';
NOCOLLISIONSYMBOL = 'O';

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], testmode: bool, expected: Any, directions: List[Tuple[int, int]], show_path: bool, **kwargs):
    m, n, trees = extract_data(lines);
    nr_collisions = [];
    for dx, dy in directions:
        path = compute_path(m, n, dx, dy);
        c = compute_collisions(trees, path);
        nr_collisions.append(c);
        if show_path:
            display_path(trees, path);
    display_solutions(testmode, expected, m, n, nr_collisions);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> Tuple[int, int, ndarray]:
    trees = [];
    for _ in lines:
        ## Do not use re.split! Otherwise empty characters appear
        trees.append([__ for __ in _]);
    m = len(trees);
    n = max([len(_) for _ in trees]);
    for i in range(m):
        trees[i] = [1*(_ == TREESYMBOL) for _ in trees[i]] + [0]*(n-len(trees[i]));
    trees = asarray(trees);
    return m, n, trees;

def compute_path(m: int, n: int, dx: int, dy: int) -> List[ndarray]:
    if dy <= 0:
        raise ValueError('Vertical direction must be positive!');
    position = asarray([0,0]);
    N = ceil(m/dy);
    t = asarray(range(N));
    x = (t*dx % n).tolist();
    y = t*dy
    path = transpose(asarray([y, x])).tolist();
    return path;

def compute_collisions(trees: ndarray, path: ndarray) -> int:
    return sum([trees[tuple(_)] for _ in path]);

def display_path(trees: ndarray, path: List[ndarray]):
    m, n = trees.shape;
    landscape = [[TREESYMBOL if trees[i, j]==1 else NOTREESYMBOL for j in range(n)] for i in range(m)];
    N = len(path);
    for i in range(N):
        x, y = path[i];
        landscape[x][y] = COLLISIONSYMBOL if trees[x, y] == 1 else NOCOLLISIONSYMBOL;
    print('  \033[4;1mPFAD DES SKIIFAHRERS\033[0m:');
    for _ in landscape:
        line = ''.join(_);
        print('  ' + line);
    print('');
    return;

def display_solutions(testmode: bool, expected: Any, m: int, n: int, nr_collisions: List[int]):
    result = prod(nr_collisions);
    print('  Auf der Skiifahrt der Höhe \033[92;1m{m}\033[0m und Breite \033[92;1m{n}\033[0m gab es \033[1m{nr_collisions}\033[0m Kollisions -> Produkt = \033[4;1m{result}\033[0m.'.format(
        m=m,
        n=n,
        nr_collisions=', '.join([str(_) for _ in nr_collisions]),
        result=result,
    ));
    if testmode:
        checkresult(expected, (nr_collisions, result));
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
