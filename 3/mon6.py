# -*- coding:utf-8 -*-
# 繰り返しでフィボナッチ数列を定義
def fib_rec(n):
  if n == 0 or n == 1:
    return n
  else:
    i = 2
    ans = 0
    fib0 = 0
    fib1 = 1
    while i < n:
      ans = fib1 + fib0
      fib0 = fib1
      fib1 = ans
      i+=1
    return fib0 + fib1

def main():
  for i in range(10):
    print(fib_rec(i))

if __name__ =="__main__":
  main()
