#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from typing import Any;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def checkresult(expected: Any, result: Any):
    if expected == result:
        print('  (\033[92;1m✔️\033[0m) \033[92;1mErwartetes Ergebnis erreicht!\033[0m'.format(expected));
    else:
        print('  Erwartetes Ergbnis: \033[94;4;1m{}\033[0m.'.format(expected));
        print('  (\033[91;1mX\033[0m) \033[91;1mErwartetes Ergebnis nicht erreicht!\033[0m');
