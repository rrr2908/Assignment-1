#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a Python program to count the number of even and odd numbers from a series of numbers.
arr = []
n = int(input("Enter number of elements:"))
for i in range(0, n):
    ele=int(input())
    arr.append(ele)
print(arr)
even = 0
odd = 0
for i in range(0, n):
    if(arr[i]%2==0):
        even = even + 1
    else:
        odd = odd + 1
print(even)
print(odd)
    


# In[3]:


#Write a Python program that accepts a word from the user and reverse it.
string = str(input("Enter the word that needs to be reversed: "))
rev = ""
for i in string:
    rev = i + rev
print(rev)


# In[8]:


#Write a Python program to get the Fibonacci series between 0 to 50
n = 50
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ")
while(count <= 50):
    
    count += 1
    a = b
    b = sum
    sum = a + b
    print(sum)


# In[ ]:




