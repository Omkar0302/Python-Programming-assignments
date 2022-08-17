import logging
import random

logging.basicConfig(filename="Programming Assignment1",level= logging.DEBUG)
logging.info("A1-Hello Python")
def Add_Div(a,b,c):
    try:
       if a ==1:
         return b+c
       elif a==2:
         return b-c
       else:
           logging.info("Type integers between 1 and 2")
           pass
    except:
        logging.info('Type integers')
        pass

def Triangle_Area(a,b):
    try:
       h=(a*b)/2
       return h
    except:
        logging.info('Type integers')
        pass
def swap(a,b):
    try:
       logging.info('%s = a',a)
       logging.info('%s= b', b)
       c=a
       a=b
       b=c
       logging.info('%s = a', a)
       logging.info('%s= b', b)
    except:
        logging.info('Type integers')
        pass

O=Add_Div(1,3,4)
logging.info('A2-%s',O)

T=Triangle_Area(2,3)
logging.info('A3-%s',T)

S=swap(1,2)
R=random.randint(0,100)
logging.info('A5-Random no. %s',R)
