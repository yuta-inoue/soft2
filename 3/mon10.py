# -*- condig:utf-8 -*-
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a % b)
def make_rat(a,b):
    g = gcd(a,b)
    return [a/g,b/g]
def numer(x):
  return x[0]
def denom(x):
  return x[1]

def print_rat(x):
  print("%d/%d" % (x[0],x[1]))

def sub_rat(x,y):
  if isinstance(x,list):
    if isinstance(y,list):
      return make_rat(numer(x)*denom(y)-numer(y)*denom(x),denom(x)*denom(y))
    else :
      return make_rat(numer(x)-y*denom(x),denom(x))
  else:
    if isinstance(y,list):
      return make_rat(x * denom(y) - numer(y),denom(y))
    else:
      return x-y

one_half = make_rat(1,2)
one_third = make_rat(1,3)
print_rat(sub_rat(one_half,one_third))
print_rat(sub_rat(1,one_half))

def div_rat(x,y):
    if isinstance(x,list):
      if isinstance(y,list):
        return make_rat(numer(x)*denom(y),denom(x)*numer(y))
      else :
        return make_rat(numer(x),denom(x)*y)
    else:
      if isinstance(y,list):
        return make_rat(x * denom(y),numer(y))
      else:
        return x/y
print_rat(div_rat(one_half,one_third))
print_rat(div_rat(1,one_half))

def add_rat(x,y):
    return make_rat(numer(x)*denom(y)+denom(x)*numer(y),denom(x)*denom(y))


print_rat(add_rat(one_third,one_third))
