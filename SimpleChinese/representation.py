import numpy as np
import pandas as pd

from lib.nlp import extract_words

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import PCA, NMF
from sklearn.cluster import KMeans, DBSCAN, MeanShift

import jieba
jieba.setLogLevel(60)

def pca(x, n_components=2):
    pca = PCA(n_components=n_components)
    return pd.Series(pca.fit_transform(list(x)).tolist(), index=x.index)

def nmf(x, n_components=2):
    nmf = NMF(n_components=n_components, init="random", random_state=0)
    return pd.Series(nmf.fit_transform(list(x)).tolist(), index=x.index)

def term_frequency(x, mode=0, max_features=None, return_feature_names=False):
    if mode not in [0,1,2,3,4]:
        """
        0: isOverlap=True, keepSingles=False
        1: isOverlap=True, keepSingles=True
        2: isOverlap=False, keepSingles=False
        3: isOverlap=False, keepSingles=True
        4: only single characters
        """
        raise ValueError("The mode should be chosen from 0-4.")
    if not isinstance(x, pd.Series):
        raise ValueError("The type of the input variable should be pandas.Series.")
    
    vectorizer = CountVectorizer(max_features=max_features,
                                 lowercase=False,
                                 token_pattern="\S+")
    y = extract_words(x, isList=False, mode=mode, token=" ")
    y = pd.Series(vectorizer.fit_transform(y).toarray().tolist(), index=x.index)

    if return_feature_names:
        return (y, tf.get_feature_names())
    else:
        return y

def tfidf(x, mode=0, max_features=None, min_df=1, return_feature_names=False):
    if mode not in [0,1,2,3,4]:
        """
        0: isOverlap=True, keepSingles=False
        1: isOverlap=True, keepSingles=True
        2: isOverlap=False, keepSingles=False
        3: isOverlap=False, keepSingles=True
        4: only single characters
        """
        raise ValueError("The mode should be chosen from 0-4.")
    if not isinstance(x, pd.Series):
        raise ValueError("The type of the input variable should be pandas.Series.")
    
    vectorizer = TfidfVectorizer(use_idf=True,
                                 max_features=max_features,
                                 min_df=min_df,
                                 token_pattern="\S+",
                                 lowercase=False,)
    y = extract_words(x, isList=False, mode=mode, token=" ")
    y = pd.Series(vectorizer.fit_transform(y).toarray().tolist(), index=y.index)
    
    if return_feature_names:
        return (y, tf.get_feature_names())
    else:
        return y
