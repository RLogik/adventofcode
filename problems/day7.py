#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
import pandas as pd;
from numpy import ndarray;
from numpy import full;
from numpy.linalg import norm;
from typing import Any;
from typing import Generator;
from typing import Dict;
from typing import List;
from typing import Tuple;

from problems.checkresult import checkresult;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], testmode: bool, expected: Any, first_part: bool, show_bags: bool, bag: str, **kwargs):
    graph = extract_data(lines);
    closure = compute_closure(graph, bag);
    if first_part:
        table  = closure[closure.subbag == bag];
        result = len(table);
        if show_bags:
            print(table);
            print('  Eine \033[92;1m{bag}\033[0m Tasche kann durch\n    {bags},\n  eingepackt werden.'.format(
                bag=bag,
                bags=('eine ' + (' oder\n    eine '.join(['\033[1m{}\033[0m'.format(row.bag) for row in table.itertuples()])) if result > 0 else 'keine') + ' Tasche',
            ));
        display_solutions1(testmode, expected, bag, result);
    else:
        table  = closure[closure.bag == bag];
        result = sum(closure[closure.bag == bag].amount);
        if show_bags:
            print(table);
            print('  Eine \033[92;1m{bag}\033[0m Tasche enthält\n     {bags}\n  Tasche/n.'.format(
                bag=bag,
                bags=((' und\n     '.join(['\033[1m{}\033[0m x \033[1m{}\033[0m'.format(row.subbag, row.amount) for row in table.itertuples()])) if result > 0 else 'keine'),
            ));
        display_solutions2(testmode, expected, bag, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> Tuple[pd.DataFrame, List[str], ndarray]:
    data: List[Dict[str, Any]] = [];
    for line in lines:
        for bag, n, subbag in get_bag_relation(line):
            data.append(dict(
                bag=bag,
                amount=n,
                subbag=subbag
            ));
    graph = pd.DataFrame(
        data=data,
        index=None,
        columns=('bag', 'subbag', 'amount')
    );
    graph = graph.astype(dict(
        bag    = 'string',
        subbag = 'string',
        amount = 'Int16',
    ));
    del data;
    return graph;

def compute_closure(graph: pd.DataFrame, bag: str) -> pd.DataFrame:
    ## Inzidenzmatrix
    V = sorted([_ for _ in set(list(graph.bag) + list(graph.subbag)) if not pd.isna(_)]);
    n = len(V);
    A = full(shape=(n, n), dtype='Int16', fill_value=0);
    for row in graph.itertuples():
        if pd.isna(row.subbag):
            continue;
        i = V.index(row.subbag);
        j = V.index(row.bag);
        A[i, j] = row.amount;

    ## transitiver Abschluss
    R = 1*A;
    for _ in range(2, n+1):
        R_new = A + A @ R;
        if norm(1*R_new - 1*R) == 0:
            break;
        R = R_new;

    ## als Dataframe speichern
    data: List[Dict[str, Any]] = [];
    for i in range(n):
        for j in range(n):
            if R[i, j] == 0:
                continue;
            data.append(dict(
                subbag=V[i],
                bag=V[j],
                amount=R[i, j],
            ));
    closure = pd.DataFrame(data=data, index=None, columns=('subbag', 'bag', 'amount'));
    closure = closure.astype(dict(bag = 'string', subbag = 'string', amount = 'Int16'));
    del data;
    return closure;

def display_solutions1(testmode: bool, expected: Any, bag: str, result: int):
    print('  Eine \033[92;1m{bag}\033[0m Tasche lässt sich in \033[4;1m{result}\033[0m Tasche/n einpacken.'.format(
        bag=bag,
        result=result,
    ));
    if testmode:
        checkresult(expected, result);
    return;

def display_solutions2(testmode: bool, expected: Any, bag: str, result: int):
    print('  Eine \033[92;1m{bag}\033[0m enthält \033[4;1m{result}\033[0m Tasche/n.'.format(
        bag=bag,
        result=result,
    ));
    if testmode:
        checkresult(expected, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def get_bag_relation(s: str) -> Generator[Tuple[str, int, str], None, None]:
    s     = re.sub(r'\.', '', s);
    s     = re.sub(r'\s*and\s*', ',', s);
    parts = re.split(r'contain(?:s|)', s);
    if len(parts) < 2:
        return;
    bag = get_bag_colour(parts[0]);
    for _ in re.split(r',+', parts[1]):
        n, subbag = get_amount_and_colour(_);
        if n < 0:
            continue;
        yield bag, n, subbag;

def get_bag_colour(s: str) -> str:
    return re.sub(r'\s+bag(?:s|)', '', s).strip();

def get_amount_and_colour(s: str) -> Tuple[int, str]:
    if re.match(r'\s*no other bag(?:s|)', s):
        return 0, pd.NA;
    m = re.match(r'\s*(0|[1-9]\d*)\s*(.*)$', s)
    if m:
        return int(m.group(1)), get_bag_colour(m.group(2));
    return -1, pd.NA;
