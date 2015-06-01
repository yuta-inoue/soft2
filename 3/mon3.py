# -*- coding:utf-8 -*-
# 3つの数を引数としてとり、大きい二つの話を返す
def add_large2(x,y,z):
  return max(x+y,max(y+z,z+x))

def main():
  print(add_large2(1,2,3))
  print(add_large2(5,3,10))

if __name__ =="__main__":
  main()
