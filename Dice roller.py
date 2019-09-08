#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as random

maximum = int(input('How many sides do you want? '))

def roll():
    print('You rolled a ' + str(random.randint(1, maximum)) + '!')
    askagain()
    
def askagain():
        reply = input('Do you wish to roll again? (yes/no) ')
        if reply == 'no':
            print('Thank you!')
        elif reply == 'yes':
            roll()
        else:
            askagain()

roll()


# In[ ]:




