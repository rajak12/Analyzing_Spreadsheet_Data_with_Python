#!/usr/bin/env python
# coding: utf-8

# # Analyzing Spreadsheet Data with Python
# 

# In[59]:


pip install openpyxl


# In[60]:


import requests
import os


# # Exercise 3: Load Data to Python!
# 

# In[61]:


df_facilities = pd.read_excel("Airport_Data.xlsx",sheet_name = "Facilities")


# # Question 1: What are the types for aviation facilities in Alaska?
# 

# In[62]:


df_facilities["Type"]


# In[63]:


df_facilities["Type"].unique()


# # Provide a table containing the information for all Seaplane Bases in Alaska

# In[64]:


df_facilities["Type"]=="SEAPLANE BASE"


# # What are the 5 highest aviation facilities in Alaska

# In[68]:


df_facilities.sort_values(by = "ARPElevation",ascending = False)


# In[69]:


df_facilities.sort_values(by = "ARPElevation",ascending = False).head(n = 5)


# # What is the average elevation of aviation facilities?

# In[72]:


df_facilities["ARPElevation"].mean()


# # What are the highest and lowest elevation values of the aviation facilities

# In[73]:


df_facilities["ARPElevation"].max()


# In[74]:


df_facilities["ARPElevation"].min()


# # Exercise 5: Write to `xlsx` Files!
# 

# In[78]:


df_s = df_facilities[df_facilities["Type"]== "SEAPLANE BASE"]


# In[79]:


df_s.to_excel("./s.xlsx")


# In[ ]:




