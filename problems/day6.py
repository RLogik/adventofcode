#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
import pandas as pd;
from typing import Any;
from typing import Dict;
from typing import List;
from typing import Tuple;

from problems.checkresult import checkresult;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], testmode: bool, expected: Any, mode: str, **kwargs):
    answers = extract_data(lines);
    answers, result = compute_result(answers, mode);
    display_solutions(testmode, expected, mode, answers, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> pd.DataFrame:
    group  = 0;
    person = 0;
    data: List[Dict[str, Any]] = [];
    for _ in lines:
        ans = re.sub(r'\s+', '', _);
        if ans == '':
            group += 1;
            person = 0;
        else:
            for q in ans:
                data.append(dict(
                    group=group,
                    groupsize=pd.NA,
                    person=person,
                    question=q,
                    matches=pd.NA,
                ));
            person += 1;
    answers = pd.DataFrame(
        data=data,
        index=None,
        columns=('group', 'groupsize', 'person', 'question', 'matches')
    );
    answers = answers.astype(dict(
        group='Int32',
        groupsize='Int32',
        person='Int32',
        question='string',
        matches='Int32',
    ));
    del data;
    # compute group-size column:
    answers.groupsize = answers.join(
            answers \
                .groupby(by=['group'], axis=0) \
                .apply(lambda x: max(x.person)+1)
                .rename('new'),
            on=['group']
        ).new;
    return answers;

def compute_result(answers: pd.DataFrame, mode: str) -> Tuple[pd.DataFrame, int]:
    ## berechne Anzahl der Personen per Gruppe, die auf dieselbe Frage antworten:
    answers.matches = answers.join(
            answers \
                .groupby(by=['group', 'question'], axis=0) \
                .apply(len)
                .rename('new'),
            on=['group', 'question']
        ).new;
    ## berechne Zusammenfassungen:
    summary = answers[['group', 'groupsize', 'question', 'matches']] \
        .drop_duplicates(subset=['group', 'question'], keep='first') \
        .reset_index();
    summary['matches_any'] = summary.apply(lambda x: x.matches > 0, axis=1);
    summary['matches_all'] = summary.apply(lambda x: x.matches == x.groupsize, axis=1);
    if mode == 'any':
        result = sum(summary.matches_any);
    else: # elif mode == 'all':
        result = sum(summary.matches_all);
    return summary, result;

def display_solutions(testmode: bool, expected: Any, mode: str, answers: pd.DataFrame, result: int):
    n = max(answers.group) + 1;
    print('  Es gab \033[92;1m{n}\033[0m Gruppe/n.\n  Die summe der eindeutigen, von {mode} beantworteten Fragen (pro Gruppe) ist \033[4;1m{result}\033[0m.'.format(
        n=n,
        mode='≥ 1 Person/en' if mode == 'any' else 'allen',
        result=result,
    ));
    if testmode:
        checkresult(expected, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
