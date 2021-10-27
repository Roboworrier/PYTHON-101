#!/usr/bin/env python
# coding: utf-8

# # Linear Search

# In[ ]:


def linear_search(item, my_list):
    i= 0
    found = False
    
    while i < len(my_list) and found == False:
         if my_list[i] == item:
                found = True
    else:
         i= i +1 
    return found


# In[ ]:


#test  = [2,345,6,7,87,8,6,5,3,5,7,8]
#print(linear_search(45,test))
#print(linear_search(87, test))


# # Binary Search
# 

# In[ ]:


def binary_search(item, my_list):
    found = False
    first = 0
    last = len(my_list)-1
    
    
    while first <= last and found == False:
        midpoint = (first+ last)//2
        if my_list[midpoint] == item:
            found = True
        else:
            if my_list[midpoint]< item:
                first = midpoint + 1
            else:
                last = midpoint -1 
return found


# In[ ]:


#test  = [2,345,6,7,87,8,6,5,3,5,7,8]
#print(binary_search(45,test))
#print(binary_search(87, test))


# # Insertion Sort
# 
# 

# In[1]:


def insertion_sort(my_list):
    n = len(my_list)
    for i in range(1,n):
        value = my_list[i]
        j = i
        while j> 0 and my_list[j-1]>value:
            my_list[j] = my_list[j-1]
            j = j -1
        my_list[j] = value
    return my_list


# In[ ]:


#test_2 = [45,677,998,3444,67,887,89,7,9]
#print(insertion_sort(test_2))


# In[ ]:




