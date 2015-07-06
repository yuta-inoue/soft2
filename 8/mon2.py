import numpy as np
from scipy import optimize

y = lambda x:x**2-2
dy = lambda x:2.*x

res = optimize.newton(y,5,dy)
print(res)
