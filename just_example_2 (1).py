#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


sales = pd.read_csv ("C:/...........sales_data.csv",sep =",")
sales


# In[4]:


sales.head()


# In[5]:


sales.shape


# In[6]:


sales.info()


# In[7]:


sales.describe()


# In[8]:


sales['Unit_Cost'].describe()


# In[9]:


sales['Unit_Cost'].mean()


# In[11]:


sales['Unit_Cost'].median()


# In[13]:


sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))


# In[14]:


sales['Unit_Cost'].plot(kind='density',figsize=(10,3))


# In[15]:


ax = sales['Unit_Cost'].plot(kind = 'density', figsize= (14,6))
ax.axvline(sales['Unit_Cost'].mean(), color= 'red')
ax.axvline(sales['Unit_Cost'].median(), color='green')


# In[16]:


ax = sales['Unit_Cost'].plot(kind='hist', figsize=(14,6))
ax.set_xlabel('x')
ax.set_ylabel('y')


# In[17]:


sales['Age_Group'].value_counts().plot(kind= 'pie', figsize=(6,6))


# In[18]:


ax=sales['Age_Group'].value_counts().plot(kind= 'bar',figsize=(14,6))
ax.set_xlabel('x')


# In[19]:


corr = sales.corr()


# In[20]:


corr


# In[21]:


fig= plt.figure(figsize=(8,8))
plt.matshow(corr, cmap = 'RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)),corr.columns, rotation= 'vertical')
plt.yticks(range(len(corr.columns)),corr.columns)


# In[24]:


sales.plot(kind='scatter',x='Customer_Age',y='Revenue', figsize=(14,8) )


# In[25]:


sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(10,8))


# In[26]:


ax= sales[['Profit','Age_Group']].boxplot( by= 'Age_Group', figsize = (10,9))
ax.set_xlabel('Profit')


# In[27]:


box_plots=['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']
sales[box_plots].plot(kind = 'box',subplots= True, layout=(3,4), figsize = (14,8))


# In[31]:


sales['revenue_per_age']=sales['Revenue'] / sales['Customer_Age']


# In[32]:


sales['revenue_per_age'].plot(kind='density', figsize=(10,5))


# In[35]:


sales.loc[sales['State'] == 'Kentucky']


# In[36]:


sales.loc[sales['Age_Group'] == 'Adults (35-64)', 'Revenue'].mean()


# In[ ]:




