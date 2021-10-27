#!/usr/bin/env python
# coding: utf-8

# # Caeser Cipher 

# In[50]:


alphabet = 'abcefghijklmnopqrstuwxyz'


# In[51]:


input_text = 'hello'


# # Build a very simple version

# In[72]:


#output = ''
'''inrange function'''
#for char in input_text :
    #alpha_index = alphabet.find(char)
    #output = output +  alphabet[alpha_index+3]
#print(output)


# # What if cipher index goes beyond end of alphabet

# In[73]:


#output = ''
'''outta range function'''
#for char in input_text:
    #alpha_index = alphabet.find(char)
    #output = output+ alphabet[alpha_index + 20]
#print(output)


# # WRITE a function  to deal with shift

# In[74]:


def shift_amount(i):
    #Will determine the shift , taking  into account the lenght of the alphabet. takes integer-
    return i%26


# # Now test with shift>26

# In[79]:


#output_1 =  ''
#for char in input_text:
    #alpha_index = alphabet.find(char)
    #outout_1 = output_1 + alphabet[shift_amount(alpha_index +30)]
#print(output_1)


# # A complete function

# In[80]:


def encrypt(text, required_shift):
    out_string = ''
    text = text.lower()
    for char in text:
        if char not in alphabet:
            out_string = out_string + char
        else:
            alpha_index = alphabet.find(char)
            out_string = out_string + alphabet[shift_amount(alpha_index +required_shift)]
    return out_string


# In[ ]:


new_string = 'Once upon'
shift = encrypt('new_string', 5)


# In[82]:


shift

