# -*- coding: utf-8 -*-
"""Python_Solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YzNsPPfYsH6y5dVdF4HhHFPkXnvn7_bP

#Task 1
"""

T = ('python',)*5

"""#Task 2"""

getStr = input("Input string: ")
for i in getStr[0:len(getStr):2]:
  print(i)

"""#Task 3"""

elements = [5,7,4,9,3,2]
avg = sum(elements)/len(elements)
print("Average",avg)

"""#Task 4"""

year = int(input("Enter year: "))
if ((year%4==0 and year%100!=0) or year%400==0):
  print(year,"is leap year.")
else:
  print(year,"is not leap year.")

"""#Taks5"""

l = [21, 6, 12, 57, 35, 61]
l.remove(max(l))
l.remove(min(l))
print("Second maximum:",max(l))
print("Second minimum:",min(l))
print("Sum of second maximum and second minimum:", (max(l)+min(l)) )