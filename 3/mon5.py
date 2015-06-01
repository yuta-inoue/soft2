# -*- coding:utf-8 -*-
# 再帰関数の線形再帰(フィボナッチ数列の線形再帰)

fib = []

# 配列の要素を先に初期化して保持しておく（ループはO(n)）
def init(n):
  fib.append(0)
  fib.append(1)
  for i in range(2,n):
    fib.append(fib[i-1] + fib[i-2])

# 先にO(n)で初期化した配列のn番目の要素を返す
def fib_linear(n):
  return fib[n]

def main():
  init(10)
  for i in range(10):
    print(fib_linear(i))

if __name__ == "__main__":
  main()
