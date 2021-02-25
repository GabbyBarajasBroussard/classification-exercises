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


def prep_iris(df):
    df= df.drop(columns=['species_id', 'measurement_id'])
    df= df.rename(columns={"species_name": "species"}, inplace= True)
    dummy_df = pd.get_dummies(df[['species']])
    df= pd.concat([iris, dummy_df], axis=1)
    return df

# In[ ]:




