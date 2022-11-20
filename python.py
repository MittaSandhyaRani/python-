#!/usr/bin/env python
# coding: utf-8

# In[1]:


def pal(num):
    x=num[::-1]
    if x==num:
        print("palindrome")
    else:
        print("not palindrome")
print(pal("madam"))


# In[4]:


a=0
b=1
n=int(input("enter no of elements"))
print(a,b,end="")
while n-2:
    c=a+b
    a=b
    b=c
    print(c,end="")
    n=n-1


# In[7]:


num=int(input("enter the num:"))
s=0
temp=num
while temp>0:
    c=temp%10
    s=s+c**3
    temp//=10
if num==s:
    print("armstrong number")
else: 
    print("mot arm strong")


# In[8]:


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
print(add(10,10))


# In[30]:


num=5
m=(2*num)-2
for i in range(0,num):
    for j in range(0,m):
        print(end=" ")
    m=m-1
    for j in range(0,i+1):
        print("*",end=' ')
    print(" ")


# In[32]:


year=int(input("enter your num:\n"))
if year%400==0:
    print('leap year')
elif year%4==0:
    print('leap year')
elif year%100==0:
    print('not a leap year')
else:
    print('not a leap year')


# In[39]:


n=int(input("enter a num:"))
for i in range(2,n):
    if n%i==0:
        print("not prime")
        break
    else:
        print("prime")
        break


# In[49]:


import math
pi=math.pi
def circle(r):
    return pi*r*r

def rectangle(r):
    return 2*pi*r
def cylinder(r,h):
    return (2*pi*r)+(2*pi*h)
def sphere(r):
    return 2*pi*r*r
def cube(side):
    return 6*side*side
print(sphere(1))


# In[53]:


a=[1,2,3,4]
print(a[::-1])


# In[ ]:




