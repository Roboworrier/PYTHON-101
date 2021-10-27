#!/usr/bin/env python
# coding: utf-8

# # Matplotlib Random Walk Project

# In[117]:


import matplotlib.pyplot as plt
from random import choice
get_ipython().run_line_magic('matplotlib', 'inline')


# ## Then we change the default setting for our plots

# In[118]:


plt.rc('figure' , figsize=(12,6))


# ## Now we create x and y values
# 

# In[119]:


values = list(range(0,55,5))
values


# ## And we plot them

# In[120]:


plt.plot(values)
plt.show()


# ## We can label the X and Y  axis and add a title

# In[121]:


x_axis = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]


# In[122]:


plt.plot(x_axis,values)
plt.xlim(0,1.0)
plt.ylim(0.50)
plt.title('our plot')
plt.xlabel('Hard work')
plt.ylabel('Success')
plt.show()


# ## We can also change the style of the plot
# 

# In[123]:


plt.plot(x_axis, values,'ko--')
plt.xlim(0,1.0)
plt.ylim(0,50)
plt.title('Customized plot')
plt.xlabel('Hard work')
plt.ylabel('Success')
plt.show


# # RANDOM Walk Function

# In[126]:


def rand_walk(step_num):
    walk = []
    step_choice = choice([1,-1])
    walk.append(step_choice)
    for i in range(1, step_num):
        step_choice_2 = choice([1,-1])
        next_step  = walk[i-1]  + step_choice_2
        walk.append(next_step)
    return walk


# In[127]:


random_w = rand_walk(100)
print((random_w))


# In[128]:


def plot_walk(walk):
    x  = list(range(1,len(walk)+1))
    
    
    plt.plot(walk)
    plt.xlabel('Number of steps')
    plt.ylabel('Distance from origin')
    plt.title('Our Random Walk')
    plt.show()


# In[129]:


plot_walk(rand_walk(1000))

