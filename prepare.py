#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

import warnings
warnings.filterwarnings("ignore")

import acquire


# In[2]:


def prep_iris(iris):
    iris= iris.drop(columns=['species_id', 'measurement_id'])
    iris= iris.rename(columns={"species_name": "species"})
    dummy_df = pd.get_dummies(iris[['species']])
    iris = pd.concat([iris, dummy_df], axis=1)
    return iris


# In[3]:


def prep_titanic(df):
    # drop missing observations of embark town
    df = df[~df.embark_town.isnull()]
    # use the pd.get_dummies to encode embark_town column
    df_dummies = pd.get_dummies(df[['sex', 'embark_town']], drop_first=True)
    df = pd.concat([df, df_dummies], axis=1)
    # Drop the embarked and deck columns
    df = df.drop(columns=['embarked', 'deck', 'passenger_id', 'class', 'sex', 'embark_town'])
    return df


# In[4]:





# In[ ]:




