#!/usr/bin/env python
# coding: utf-8

# In[4]:


#A1:
def Kilometers_miles(a):
    try:
        b=a*0.621
        return b
    except:
        pass
m=Kilometers_miles(2)
print(m,"miles")


# In[5]:


#A2:
def celsius_farenheit(c):
    try:
        fa=(c*1.8)+32
        return fa
    except:
        pass
f=celsius_farenheit(25)
print(f,"Farenheit")


# In[6]:


#A3:
import calendar

y= 2022
m= 8
print(calendar.month(y,m))


# In[13]:


#A4:
import math
 
def quadratic_equation(a,b,c):
    try:
        d = (b**2) - 4* a*c
        if d < 0: 
            return 'The equation has no real solution'
        elif d == 0:
            x = (-b)/(2*a) 
            return'This equation has one solution: ',x
        else: 
            x1 = (-b+math.sqrt(d))/(2*a) 
            x2 = (-b-math.sqrt(d))/(2*a) 
            return 'This equation has two solutions: ',x1, 'or', x2
    except:
        pass
    

q=quadratic_equation(int(input("Enter a for ax**2 + bx + c.")),int(input("Enter b for ax**2 + bx + c.")),int(input("Enter c for ax**2 + bx + c.")))
print(q)


# In[18]:


#A5
def swap_wo_variable(a,b):
    try:
        a=a+b
        b=a-b
        a=a-b
        return 'a=',a,'b=',b
    except:
        pass
s=swap_wo_variable(int(input("a =")), int(input("b=")))
print(s)


# 
