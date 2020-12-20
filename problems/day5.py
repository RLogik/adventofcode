#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
import pandas as pd;
from typing import Any;
from typing import List;
from typing import Dict;

from problems.checkresult import checkresult;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], testmode: bool, expected: Any, show_boardingcodes: bool, first_part: bool, **kwargs):
    boarding = extract_data(lines);
    boarding = compute_ids(boarding);
    if show_boardingcodes:
        display_boardingcoddes(boarding);
    if first_part:
        result = get_maximal_id(boarding);
    else:
        result = get_missing_id(boarding);
    display_solutions(testmode, expected, boarding, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> pd.DataFrame:
    data: List[Dict[str, Any]] = [];
    for line in lines:
        if not re.match(r'^[FB]+[LR]+$', line):
            continue;
        data.append(dict(
            partition=line,
            row_code=pd.NA,
            col_code=pd.NA,
            row=pd.NA,
            col=pd.NA,
            id=pd.NA
        ));
    boarding = pd.DataFrame(
        data=data,
        index=None,
        columns=('partition', 'row_code', 'col_code', 'row', 'col', 'id')
    );
    boarding = boarding.astype(dict(
        partition='string',
        row_code='string',
        col_code='string',
        row='Int8',
        col='Int8',
        id='Int8'
    ));
    del data;
    return boarding;

def compute_ids(boarding: pd.DataFrame):
    def decode(zero: str, one: str):
        return lambda x: ''.join([('0' if _ == zero else ('1' if _ == one else '')) for _ in x]);
    boarding.row_code = boarding.partition.apply(decode(zero='F', one='B'));
    boarding.col_code = boarding.partition.apply(decode(zero='L', one='R'));
    boarding.row = boarding.row_code.apply(lambda x: int(x, 2));
    boarding.col = boarding.col_code.apply(lambda x: int(x, 2));
    boarding.id = boarding.apply(lambda e: int(e.row_code + e.col_code, 2), axis=1);
    # boarding = boarding.drop(['partition'], axis=1);
    boarding = boarding \
            .sort_values(by=('id'), ascending=True) \
            .reset_index();
    return boarding;

def get_missing_id(boarding: pd.DataFrame) -> int:
    ids = sorted(list(boarding.id));
    id_max = max([0] + ids);
    missing = [_ for _ in range(id_max + 1) if not _ in ids and (_ - 1 in ids) and (_ + 1 in ids)] + [pd.NA];
    id = missing[0];
    if not pd.isna(id):
        print(boarding[boarding.id.isin([id-1, id+1])]);
    return id;

def get_maximal_id(boarding: pd.DataFrame) -> int:
    return max(boarding.id);

def display_boardingcoddes(boarding: pd.DataFrame):
    print('  \033[4;1mBOARDING CODES\033[0m:');
    print(boarding);
    print('');
    return;

def display_solutions(testmode: bool, expected: Any, boarding: pd.DataFrame, result: int):
    n = len(boarding);
    print('  Es gab \033[92;1m{n}\033[0m Boardingcodes. Die gesuchte ID ist \033[4;1m{result}\033[0m.'.format(
        n=n,
        result=result,
    ));
    if testmode:
        checkresult(expected, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
