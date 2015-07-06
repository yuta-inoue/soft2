import numpy as np
twopi = 2.0*np.pi

def NonAuto(x,t=0,gamma=1.0,omega=1.0,eps=1.0,omega2=np.sqrt(2.0)):
    def ft(t):
        return eps*np.cos(omega2*t)

    x0 = x[1]
    x1 = -gamma*x[1] -(omega**2)*x[0] - ft(t)
    return np.array([x0,x1])
