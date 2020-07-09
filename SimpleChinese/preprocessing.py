import re

import numpy as np
import pandas as pd

def _parse(func, x):
    if isinstance(x, str):
        return func(x)
    elif isinstance(x, pd.DataFrame):
        return x.applymap(func)
    else:
        raise ValueError("The type of the input variable should be string or pandas.DataFrame.")

def only_digits(x):
    
    def func(_s):
        return "".join([x for x in re.findall(r'[0-9]', _s)])
    return _parse(func, x)

def only_zh(x):
    
    def func(_s):
        return "".join([x for x in re.findall(r'[\u4e00-\u9fff]+', _s)])
    return _parse(func, x)

def only_en(x):
    
    def func(_s):
        return re.sub(r'[^\x41-\x5A\x61-\x7A ]', '', _s)
    return _parse(func, x)

def remove_space(x):
    
    def func(_s):
        return "".join(_s.split())
    return _parse(func, x)

def remove_digits(x):
    
    def func(_s):
        return re.sub('[0-9]', '', _s)
    return _parse(func, x)

def remove_zh(x):
    
    def func(_s):
        return re.sub(r'[\u4e00-\u9fff]+', '', _s)
    return _parse(func, x)

def remove_en(x):
    
    def func(_s):
        return re.sub(r'[\x41-\x5A\x61-\x7A]', '', _s)
    return _parse(func, x)

def remove_punctuations(x):
    
    def func(_s):
        return re.sub(r'[^\w\s]','',_s)
    return _parse(func, x)

def fillna(x):
    return x.fillna("")
#     return x.applymap(lambda a: a if pd.notnull(a) else "")

def toLower(x):
    
    def func(_s):
        return _s.lower()
    return _parse(func, x)
    
def toUpper(x):
    
    def func(_s):
        return _s.upper()
    return _parse(func, x)

def clean(x):
    y = fillna(x)
    y = toLower(y)
    y = remove_punctuations(y)
    y = remove_space(y)
    return y
