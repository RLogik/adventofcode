#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CHECKS:
# ~~~~~~~
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import re;
import pandas as pd;
from typing import Any;
from typing import Dict;
from typing import List;

from problems.checkresult import checkresult;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MAIN METHOD
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main(lines: List[str], testmode: bool, expected: Any, simple_check: bool, show_passports: bool, **kwargs):
    passports = extract_data(lines);
    if simple_check:
        passports = check_validity_simple(passports);
    else:
        passports = check_validity(passports);
    if show_passports:
        display_passports(passports);
    display_solutions(testmode, expected, passports);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SECONDARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def extract_data(lines: List[str]) -> pd.DataFrame:
    passports = [];
    passport = '';
    n = len(lines);
    data: List[Dict[str, Any]] = [];
    for k, _ in enumerate(lines):
        if not(_ == ''):
            passport += ' ' + _;
        if _ == '' or k == n-1:
            if passport == '':
                continue;
            fields = { _: __ for _, __ in re.findall(r'(\S+)\s*:\s*(\S+)', passport.strip())};
            data.append(dict(
                byr=fields['byr'] if 'byr' in fields else None,
                iyr=fields['iyr'] if 'iyr' in fields else None,
                eyr=fields['eyr'] if 'eyr' in fields else None,
                hgt=fields['hgt'] if 'hgt' in fields else None,
                hcl=fields['hcl'] if 'hcl' in fields else None,
                ecl=fields['ecl'] if 'ecl' in fields else None,
                pid=fields['pid'] if 'pid' in fields else None,
                cid=fields['cid'] if 'cid' in fields else None,
                valid=True,
            ));
            passport = '';
    passports = pd.DataFrame(
        data=data,
        index=None,
        columns=('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid', 'valid')
    );
    passports = passports.astype(dict(
        byr='string',
        iyr='string',
        eyr='string',
        hgt='string',
        hcl='string',
        ecl='string',
        pid='string',
        cid='string',
        valid='bool'
    ));
    del data;
    return passports;

def check_validity_simple(passports: pd.DataFrame) -> pd.DataFrame:
    passports.valid = passports \
        .drop(['cid'], axis=1) \
        .apply(lambda row: sum(row.isna()) == 0, axis = 1);
    return passports;

def check_validity(passports: pd.DataFrame) -> pd.DataFrame:
    passports.valid = passports \
        .drop(['cid'], axis=1) \
        .apply(lambda row: sum(row.isna()) == 0, axis = 1);

    def in_interval(a, b):
        return lambda x: a <= x and x <=b;

    def matches_pattern(p, convert=None, check=None):
        if callable(convert) and callable(check):
            def f(x):
                m = re.match(p, x);
                return not not m and check(convert(m.group(1)));
        else:
            def f(x):
                m = re.match(p, x);
                return not not m;
        return f;


    check = matches_pattern(r'^([1-9]\d{3})$', int, in_interval(1920, 2002));
    passports.valid = passports.apply(lambda row: row.valid and check(row.byr), axis=1);
    passports.byr = pd.to_numeric(passports.byr, errors='coerce');
    passports = passports.astype(dict(byr='Int32'));

    check = matches_pattern(r'^([1-9]\d{3})$', int, in_interval(2010, 2020));
    passports.valid = passports.apply(lambda row: row.valid and check(row.iyr), axis=1);
    passports.iyr = pd.to_numeric(passports.iyr, errors='coerce');
    passports = passports.astype(dict(iyr='Int32'));

    check = matches_pattern(r'^([1-9]\d{3})$', int, in_interval(2020, 2030));
    passports.valid = passports.apply(lambda row: row.valid and check(row.eyr), axis=1);
    passports.eyr = pd.to_numeric(passports.eyr, errors='coerce');
    passports = passports.astype(dict(eyr='Int32'));

    check_cm = matches_pattern(r'^(0|[1-9]\d*)(?:cm|)$', int, in_interval(150, 193));
    check_in = matches_pattern(r'^(0|[1-9]\d*)in$', int, in_interval(59, 76));
    passports.valid = passports.apply(lambda row: row.valid and (check_cm(row.hgt) or check_in(row.hgt)), axis=1);

    check = matches_pattern(r'^\#[0-9a-f]{6}$');
    passports.valid = passports.apply(lambda row: row.valid and check(row.hcl), axis=1);

    check = lambda x: x in ['amb','blu','brn','gry','grn','hzl','oth'];
    passports.valid = passports.apply(lambda row: row.valid and check(row.ecl), axis=1);

    check = matches_pattern(r'^\d{9}$');
    passports.valid = passports.apply(lambda row: row.valid and check(row.pid), axis=1);
    return passports;

def display_passports(passports: pd.DataFrame):
    print('  \033[4;1mPÄSSE\033[0m:');
    print(passports);
    print('');
    print('  \033[4;1mVORHANDENE / FEHLENDE EINTRÄGE\033[0m:');
    print(
        passports \
            .drop(['valid'], axis=1) \
            .apply(lambda col: (sum(1-col.isna()), sum(col.isna())), axis = 0)
    );
    return;

def display_solutions(testmode: bool, expected: Any, passports: pd.DataFrame):
    n = len(passports);
    result = sum(1*passports.valid);
    print('  Es gab \033[92;1m{n}\033[0m Pässe und davon sind \033[4;1m{result}\033[0m gültig.'.format(
        n=n,
        result=result,
    ));
    if testmode:
        checkresult(expected, result);
    return;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# AUXLIARY METHODS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
