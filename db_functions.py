#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import *
import warnings
warnings.filterwarnings('ignore')

db = create_engine('sqlite:///DBTest1.db', echo=True)

metadata = MetaData(db)

news = Table('news', metadata,
            Column('id', Integer, primary_key=True),
            Column('paperName', String(100)),
            Column('title', String(250)),
            Column('summary', String(10000000))
            )
news.create()


# In[ ]:




