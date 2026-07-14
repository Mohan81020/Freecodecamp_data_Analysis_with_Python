#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


def calculate(lst):
    if len(lst) < 9:
        print("ValueError: List must contain nine numbers.")
    matrix = np.array(lst).reshape(3,3)
    calculation = {
        'mean' : [matrix.mean(axis = 0).tolist(),
                  matrix.mean(axis = 1).tolist(),
                  matrix.mean().tolist],
        'variance' : [matrix.var(axis = 0).tolist(),
                      matrix.var(axis= 1).tolist(),
                      matrix.var().tolist()],
        'standard deviation' : [matrix.std(axis = 0).tolist(),
                               matrix.std(axis = 1).tolist(),
                               matrix.std().tolist()],
        'max': [matrix.max(axis = 0).tolist(),
               matrix.max(axis = 1).tolist(),
               matrix.max().tolist()],
        'min': [matrix.min(axis = 0).tolist(),
               matrix.min(axis = 1).tolist(),
               matrix.min().tolist()],
        'sum': [matrix.sum(axis = 0).tolist(),
               matrix.sum(axis = 1).tolist(),
               matrix.sum().tolist()]
        
    }
    
    return calculation


# In[3]:


lst = [0,1,2,3,4,5,6,7,8]
calculate(lst)


# In[5]:





# In[ ]:




