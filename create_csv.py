#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

with open('summary_data.csv', mode='w') as f:
    
    fieldnames = ['paper_name', 'article_title', 'summary']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()


# In[ ]:




