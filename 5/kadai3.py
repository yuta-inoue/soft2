# -*- coding:utf-8 -*-

class Rat:
    numerator = 0
    denominator = 0

    def __init__(self,numerator,denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self,other):
        return Rat(self.numerator*other.denominator+self.denominator*other.numerator,self.denominator*other.denominator)
    def mul(self,other):
        return Rat(self.numerator * other.numerator,self.denominator*other.denominator)
    def put(self):
        print("%d / %d"%(self.numerator,self.denominator))
    def reduction(self):
        g = gcd(self.numerator,self.denominator)
        if self.denominator / g == 1:
            return self.numerator / g
        else :
            return Rat(self.numerator/ g,self.denominator/g)
def put(rat):
    print("%d / %d"%(rat.numerator,rat.denominator))

def linear_combination(rat1,rat2,rat3,rat4):
    r1 = None
    r2 = None
    if isinstance(rat1,Rat):
        if isinstance(rat3,Rat):
            r1 = rat1.mul(rat3)
        else :
            r1 = Rat(rat1.numerator + rat3 * rat1.denominator,rat1.denominator)
    else:
        if isinstance(rat3,Rat):
            r1 = Rat(rat3.numerator + rat1 * rat3.denominator,rat3.denominator)
        else :
            r1 = Rat(rat1 * rat3,1)
    if isinstance(rat2,Rat):
        if isinstance(rat4,Rat):
            r2 = rat2.mul(rat4)
        else :
            r2 = Rat(rat2.numerator + rat4 * rat2.denominator,rat2.denominator)
    else:
        if isinstance(rat4,Rat):
            r2 = Rat(rat4.numerator + rat2 * rat4.denominator,rat4.denominator)
        else :
            r2 = Rat(rat2 * rat4,1)
    return (r1+r2).reduction()

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a
