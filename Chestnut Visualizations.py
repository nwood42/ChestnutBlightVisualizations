#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


df = pd.read_csv("C:/Users/there/OneDrive/Documents/Chestnut_Newspaper.csv")


# In[12]:


df.info()


# In[14]:


ax = df.plot.bar(stacked=True)


# In[15]:


df2 = df.set_index('Date')


# In[16]:


ax = df2.plot.bar(stacked=True)


# In[17]:


import matplotlib as mpl
import seaborn as sns
sns.set()
import re
get_ipython().run_line_magic('matplotlib', 'notebook')


# In[34]:


#instructions from https://sharkcoder.com/data-visualization/mpl-stacked-bars
font_color = '#525252'
csfont = {'fontname':'Georgia'} # title font
hfont = {'fontname':'Calibri'} # main font
colors = ['mediumseagreen', 'gold', 'red']


# In[35]:


ax = df2.iloc[:, 0:4].plot.barh(align='center', stacked=True, figsize=(10, 6), color=colors)
plt.tight_layout()


# In[36]:


ax = df2.iloc[:, 0:4].plot.bar(align='center', stacked=True, figsize=(10, 6), color=colors)
plt.tight_layout()


# In[37]:


ax = df2.iloc[:, 0:4].plot.bar(align='center', stacked=True, figsize=(10, 6), color=colors)
ax.set_facecolor('white')
plt.tight_layout()


# In[44]:


ax = df2.iloc[:, 0:4].plot.bar(align='center', stacked=True, figsize=(10, 6), color=colors)
ax.set_facecolor('white')
title = plt.title('Number of Identified Newspaper Articles by Date', pad=60, fontsize=18, color=font_color, **csfont)
title.set_position([.5, 1.02])
plt.subplots_adjust(top=0.8, left=0.26)
plt.xlabel("Date")
plt.ylabel("Count of Articles")
plt.tight_layout()


# In[45]:


filename = 'Chestnut_Newspapers'
plt.savefig('C:/Users/there/OneDrive/Documents/'+filename+'.png')


# In[51]:


df_all = pd.read_csv("C:/Users/there/OneDrive/Documents/Chestnut_All.csv")


# In[52]:


df_all.info()


# In[48]:


#it will be necessary to fill all blank cells in csv with "0" to create a Dtype of integer


# In[53]:


df_all2 = df_all.set_index('Date')


# In[54]:


ax2 = df_all2.iloc[:, 0:4].plot.bar(align='center', stacked=True, figsize=(10, 6), color=colors)
ax2.set_facecolor('white')
title = plt.title('Number of Identified Records by Date', pad=60, fontsize=18, color=font_color, **csfont)
title.set_position([.5, 1.02])
plt.subplots_adjust(top=0.8, left=0.26)
plt.xlabel("Date")
plt.ylabel("Count of Records")
plt.tight_layout()


# In[55]:


filename = 'Chestnut_All'
plt.savefig('C:/Users/there/OneDrive/Documents/'+filename+'.png')


# In[ ]:




