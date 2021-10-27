#!/usr/bin/env python
# coding: utf-8

# # Sierpinski Triangle
# ### First  Transformation         
# ### Must try

# In[3]:


import matplotlib.pyplot as plt
from random import choice
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


def trans_1(p):
    x= p[0]
    y= p[1]
    x1 = 0.5*x
    y1 = 0.5*y
    return x1,y1


def trans_2(p):
    x= p[0]
    y = p[1]
    x1 =0.5*x + 0.5
    y1 = 0.5*y+ 0.5
    return x1,y1

def trans_3(p):
    x= p[0]
    y=p[1]
    x1 = 0.5*x + 1
    y1 = 0.5*y
    return x1,y1

transformations = [trans_1, trans_2,trans_3]
a1 = [0]
b1 = [0]
a,b = 0,0

for i in range(10000):
    trans = choice(transformations)
    a,b = trans((a,b))
    a1.append(a)
    b1.append(b)


# In[ ]:


plt.rc('figure',figsize*(16,16))


# In[11]:


plt.plot(a1,b1,'o')


# In[ ]:




