#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education-num",
    "marital-status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital-gain",
    "capital-loss",
    "hours-per-week",
    "native-country",
    "salary"
]

df = pd.read_csv(
    r"E:\FreeCodeCamp\adult (1)\adult.data",
    names=columns,
    sep=",",
    skipinitialspace=True
)


# In[3]:


df.info()


# In[4]:


df.head()


# In[5]:


#Q1 Answer:

race_count = df['race'].value_counts()
race_count


# In[6]:


# Q2 Answer:

avg_age_of_man = df[df['sex'] == 'Male']['age'].mean()
avg_age_of_man


# In[7]:


#What is the percentage of people who have a Bachelor's degree?
# Q3 Answer: 

Bachelor_degree_holder = len(df[df['education'] == 'Bachelors'])
total_record = len(df)
percentage_Bachelor_degree_holder =round((Bachelor_degree_holder/total_record) * 100,2)
percentage_Bachelor_degree_holder


# In[8]:


# What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?


# In[9]:


df_new = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
round((df_new[df_new['salary'] == '>50K'].shape[0]/df.shape[0])*100,2)


# In[10]:


# What percentage of people without advanced education make more than 50K?

advance_education = ['Bachelors','Masters','Doctorate']
df_new = df[~df['education'].isin(advance_education)]

round((df_new[df_new['salary'] == '>50K'].shape[0]/df.shape[0])*100,2)


# In[11]:


# What is the minimum number of hours a person works per week?
Min_hrs_person_work_per_week = df['hours-per-week'].min()
Min_hrs_person_work_per_week


# In[12]:


# What percentage of the people who work the minimum number of hours per week 
# have a salary of more than 50K?


# In[13]:


df_new = df[df['hours-per-week'] == Min_hrs_person_work_per_week]
percentage_of_people = round((df_new[df_new['salary'] == '>50K'].shape[0]/df_new.shape[0])*100,2)

percentage_of_people


# In[14]:


# What country has the highest percentage of people that earn >50K and what is that percentage?

country_total = df.groupby("native-country").size()
country_rich = df[df["salary"] == ">50K"].groupby("native-country").size()
country_percentage = (country_rich / country_total) * 100
highest_earning_country = country_percentage.idxmax()

highest_earning_country_percentage = round(country_percentage.max(), 1)

print(highest_earning_country)
print(highest_earning_country_percentage)


# In[15]:





# In[29]:


# Identify the most popular occupation for those who earn >50K in India.
df_new = df[df["native-country"] == "India"]

occupation_count = (
    df_new[df_new["salary"] == ">50K"]
    .groupby("occupation")
    .size().sort_values(ascending = False)
)

print(occupation_count)

most_popular_occupation = occupation_count.idxmax()
print( most_popular_occupation)


# In[ ]:





# In[ ]:




