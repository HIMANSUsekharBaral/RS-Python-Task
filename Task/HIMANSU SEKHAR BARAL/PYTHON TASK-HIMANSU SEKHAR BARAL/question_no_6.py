# -*- coding: utf-8 -*-
"""question no 6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ENvIP0dmZWtyMRtHHS3MG79GwJSdcsbB
"""

l=int(input("enter the no of element:"))
li=[]
for i in range (0,l):
    ele=input("enter the element:")
    li.append(ele)
print(li)
prime=[]
for i in range(0,len(li)):
  count=0
  for j in range(1,i):
    if i%j==0:
      count=count+1
  if count==1:
    prime.append(i)

a=sorted(prime)
print(a)
min=a[0]
max=a[-1]
diff=max-min
print(diff)

