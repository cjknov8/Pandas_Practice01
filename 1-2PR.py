# -*- coding: utf-8 -*-
"""
Created on Mon May 10 16:57:52 2021

@author: 오후worker
"""

import pandas as pd

list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

print('\n')

idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)
