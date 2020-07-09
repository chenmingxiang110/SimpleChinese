import re
import pickle
import warnings

import numpy as np
import pandas as pd

import jieba
jieba.setLogLevel(60)

with open('names.pickle', 'rb') as handle:
    names = pickle.load(handle)
_nr = names['nr'] | names['nrt'] | names['nrfg']
_ns = names['nrt'] | names['ns'] | names['nt']
_n = set([])
for k in names.keys(): _n = _n | names[k]

def extract_nums(x, isList=False, dtype=float):
        
    def get_nums(x):
        def get_float(element):
            try:
                return float(element)
            except ValueError:
                return None
        nums = [get_float(n) for n in re.sub('[^0-9.]',' ', x).split()]
        nums = np.array([n for n in nums if n is not None]).astype(dtype)
        return list(nums)
        
    def func(x):
        nums = get_nums(x)
        if isList: return nums
        return " ".join([str(n) for n in nums])
    
    if isinstance(x, str):
        return get_nums(x)
    elif isinstance(x, pd.DataFrame):
        return x.applymap(func)
    elif isinstance(x, pd.Series):
        return x.apply(func)
    else:
        raise ValueError("The type of the input variable should be string, pd.Series, pandas.DataFrame.")
        
def extract_words(x, isList=False, mode=0, token="/"):
    
    if mode not in [0,1,2,3,4]:
        """
        0: isOverlap=True, keepSingles=False
        1: isOverlap=True, keepSingles=True
        2: isOverlap=False, keepSingles=False
        3: isOverlap=False, keepSingles=True
        4: only single characters
        """
        raise ValueError("The mode should be chosen from 0-4.")
        
    def get_words(_s):
        if mode in [0,1]:
            words = jieba.cut_for_search(_s)
        elif mode in [2,3]:
            words = jieba.cut(_s, cut_all=False)
        else:
            words = [n for n in _s]
        if mode in [1,3,4]:
            result = list(words)
        else:
            result = [n for n in words if len(n)>1]
        return result
        
    def func(x):
        words = get_words(x)
        if isList: return words
        return token.join([str(n) for n in words])
    
    if isinstance(x, str):
        return get_words(x)
    elif isinstance(x, pd.DataFrame):
        return x.applymap(func)
    elif isinstance(x, pd.Series):
        return x.apply(func)
    else:
        raise ValueError("The type of the input variable should be string, pd.Series, pandas.DataFrame.")
        
def extract_nouns(x, isList=False, split_mode=0, extract_mode="all", token="/"):
    
    if split_mode not in [0,1,2,3,4]:
        """
        0: isOverlap=True, keepSingles=False
        1: isOverlap=True, keepSingles=True
        2: isOverlap=False, keepSingles=False
        3: isOverlap=False, keepSingles=True
        4: only single characters
        """
        raise ValueError("The mode should be chosen from 0-4.")
    if extract_mode.lower() not in ["all", "person", "place"]:
        raise ValueError("The mode should be chosen from \"all\", \"person\", and \"place\".")
    if extract_mode in ["person", "place"]:
        warnings.warn("The function of extracting people or locations` names is still under developing...")
        
    def get_words(_s):
        if split_mode in [0,1]:
            words = jieba.cut_for_search(_s)
        elif split_mode in [2,3]:
            words = jieba.cut(_s, cut_all=False)
        else:
            words = [n for n in _s]
        if split_mode in [1,3,4]:
            result = list(words)
        else:
            result = [n for n in words if len(n)>1]
        
        if extract_mode=="person":
            result = [n for n in result if n in _nr]
        elif extract_mode=="place":
            result = [n for n in result if n in _ns]
        else:
            result = [n for n in result if n in _n]
        return result
        
    def func(x):
        words = get_words(x)
        if isList: return words
        return token.join([str(n) for n in words])
    
    if isinstance(x, str):
        return get_words(x)
    elif isinstance(x, pd.DataFrame):
        return x.applymap(func)
    elif isinstance(x, pd.Series):
        return x.apply(func)
    else:
        raise ValueError("The type of the input variable should be string, pd.Series, pandas.DataFrame.")
