#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[4]:


data= pd.read_csv("Olympics.csv")


# In[5]:


data


# In[6]:


data.shape


# In[7]:


pd.crosstab(data.name,data.medal)


# In[8]:


data.name.nunique()


# In[9]:


pd.crosstab(data.name,data.medal=="Gold")


# In[10]:


data.columns


# In[11]:


pd.crosstab(data.team,data.medal)


# In[12]:


athlete_medals = data.groupby('name').size()
most_medals_athlete = athlete_medals.idxmax()
most_medals_athlete


# In[13]:


freestyle_events = data[data['event'].str.contains('Freestyle')]
freestyle_events.event


# In[14]:


athlete_medals = data.groupby('name').size().sort_values(ascending=False).head(3)
athlete_medals


# In[15]:


a = data.groupby(['year', 'name']).size()
x = a[a > 1]
x


# In[16]:


x = data[data["medal"]=="Silver"]
x.name.unique()


# In[17]:


a = data.groupby(['medal']).size()
b= a[a>50]
b


# In[18]:


a = data.groupby(['name','medal']).size()
a.aggregate


# In[19]:


a = data.groupby(['team','sport']).size()
b = a.groupby(['team']).size()
c = b[b>10]
c


# In[ ]:




