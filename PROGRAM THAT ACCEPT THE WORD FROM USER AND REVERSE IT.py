#!/usr/bin/env python
# coding: utf-8

# In[45]:


#taking input for reverse word 

#using for loop for iterating the string 

#using a range function for the iteration and len function to restrict the iteration to its length using the  -1,-1,-1 for reverse the strings of word

#printing the word and using indexing [i] for taking the index value of the word to print it from reverse 

#using end="" for avoiding the output in next line

word = input('input a word for reverse ')

for i in range (len(word)-1,-1,-1):
    print(word[i]  ,end="")
   


# In[31]:





# In[ ]:




