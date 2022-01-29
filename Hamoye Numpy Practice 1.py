#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
arr=[1,2,3,4,5,6]
arr_np = np.array(arr)
print(type(arr))
print(type(arr_np))
print(arr_np.shape)


# In[8]:


a=[[1,2,3],[4,5,6],[7,8,9]]
b= np.array(a)
b


# In[9]:


b.shape


# In[10]:


b.dtype


# In[12]:


type(b)


# In[17]:


np.eye(2,2)


# In[18]:


np.zeros(5)


# In[25]:


np.full((5,4),3)


# In[26]:


np.full(4,3)


# In[31]:


np.empty(4)


# In[33]:


np.random.rand(5,5)


# In[34]:


np.random.randn(5,5)


# In[38]:


np.random.randint(1,5,5)


# In[40]:


np.random.randint(1,21,20).reshape(5,4)


# In[41]:


c=np.array([[9,8,7],[1,2,3]])
d= np.array([[4,5,6],[9,8,7]])
c+d


# In[42]:


c/d


# In[43]:


c*d


# In[44]:


c//d


# In[45]:


5/d


# In[46]:


c*2


# In[47]:


e= [5,6,7,8]
e*2


# In[49]:


#INDEXING WITH ARRAYS
d


# In[50]:


d[0]


# In[51]:


d[0,1]


# In[53]:


d[:,1:]


# In[ ]:




