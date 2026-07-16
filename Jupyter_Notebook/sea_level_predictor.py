#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


df = pd.read_csv("E:\FreeCodeCamp\epa-sea-level.csv")
df.head(10)


# In[6]:


df.info()


# In[9]:


import matplotlib.pyplot as plt

plt.scatter(
    df["Year"],
    df["CSIRO Adjusted Sea Level"]
)

plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")

plt.show()


# In[15]:


from scipy.stats import linregress

result = linregress(
    df["Year"],
    df["CSIRO Adjusted Sea Level"]
)


# In[16]:


result.slope


# In[17]:


df[["Year", "CSIRO Adjusted Sea Level"]].isnull().sum()


# In[18]:


df[df["CSIRO Adjusted Sea Level"].isna()]


# In[19]:


df_clean = df.dropna(subset=["CSIRO Adjusted Sea Level"])


# In[20]:


df_clean[["Year", "CSIRO Adjusted Sea Level"]].isnull().sum()


# In[21]:


result = linregress(
    df_clean["Year"],
    df_clean["CSIRO Adjusted Sea Level"]
)

print(result.slope)
print(result.intercept)


# In[22]:


x = np.arange(1880,2051)
y = result.slope*x + result.intercept
y


# In[32]:


plt.plot(
    x,
    y,
    color="red"
)

plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.show()


# In[27]:


df = df_clean
df_2000 = df[df["Year"] >= 2000]

result2 = linregress(
    df_2000["Year"],
    df_2000["CSIRO Adjusted Sea Level"]
)


# In[28]:


result2


# In[29]:


x2 = np.arange(2000,2051)
y2 = result2.slope*x2 + result2.intercept
y2


# In[33]:


plt.plot(
    x2,
    y2,
    color="green"
)

plt.title("Rise in Sea Level")
plt.xlabel("Year")
plt.ylabel("Sea Level (inches)")
plt.show()


# In[ ]:




