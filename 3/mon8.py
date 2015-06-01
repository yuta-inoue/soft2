# -*- coding:utf-8 -*-
def square(x):
  return x**2
def sum_squares1(x,y):
  return square(x) + square(y)

def sum_squares2(x,y):
  item = [x,y]
  item =map(square,item)
  print(item)
  return sum(item)

print(sum_squares1(3,4))
print(sum_squares2(10,11))
