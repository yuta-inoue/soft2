# -*- coding:utf-8 -*-
#
import math

step = 1.0
def abs(x):
  if x >= 0:
    return x
  else :
    return -x

def good_enough(guess,x):
  return (abs(guess**2-step)/abs(x)) < 0.001

def sqrt_iter(guess, x):
  if good_enough(guess,x):
    return guess
  else:
    return sqrt_iter(improve(guess,x))

def improve(guess, x):
  step = guess
  return (guess + (x/guess))/2

def my_sqrt(x):
  return sqrt_iter(1.0,x)

def main():
  print(my_sqrt(10))

if __name__=="__main__":
  main()
