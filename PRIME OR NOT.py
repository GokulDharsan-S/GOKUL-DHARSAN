#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def op(opp):
    i=0
    for j in range(1,opp+1):
        if opp%j==0:
            i+=1
    if i==2:
        print("It is prime")
    else:
        print("Not a prime")
op(int(input()))


# In[ ]:





# In[ ]:




