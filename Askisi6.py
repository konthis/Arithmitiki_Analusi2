from numpy import pi,sin
import random

class Exercise6:

    points = [(0,sin(0)),
              (pi/20, sin(pi/20)),
              (pi/18, sin(pi/18)),
              (pi/15, sin(pi/15)),
              (pi/14, sin(pi/14)),
              (pi/11, sin(pi/11)),
              (pi/9, sin(pi/9)),
              (pi/7.5, sin(pi/7.5)),
              (pi/5, sin(pi/5)),
              (pi/4, sin(pi/4)),
              (pi/3, sin(pi/3)),
              (pi/2,sin(pi/2))]
    a = 0
    b = pi/2
    n = 10

    def calculateFx(self):
    # n is number of parabols and NOT amount of points
        x = [self.a+i*(self.b-self.a)/self.n for i in range(self.n+1)] 
        y = [self.f(xi) for xi in x]
        return y

    def f(self,x): return sin(x)

    def Simpson(self):
        y = self.calculateFx()
        sum = y[0] + y[self.n]
        for i in range(1, self.n):
            if i%2==0:
                sum += 2*y[i]
            else:
                sum += 4*y[i]
        In = ((self.b-self.a)/(3*self.n))*sum

        # f''''(x) = sinx
        # |Max(f), xE(0/pi/2| = f(pi/2)
        M = sin(pi/2)
        e = (((self.b-self.a)**5)*M)/(180*(self.n**4))

        # Actual F, a=0, b=pi/2, F = cos(x), Fab = 1 - 0 = 1
        print("Theoretical error: ", e)
        print("Numeric error: ", abs(1-In))

        return In
    
    def TrapezoidRule(self):
        y = self.calculateFx()
        sum = y[0] + y[self.n]
        for i in range(1,self.n):
            sum += 2*y[i]
        In = ((self.b-self.a)/(2*self.n))*sum

        # f''(x) = -sinx
        # |Max(f), xE(0/pi/2| = f(pi/2)

        M = sin(pi/2)
        e = (((self.b-self.a)**3)*M)/(12*(self.n**2))

        # Actual F, a=0, b=pi/2, F = cos(x), Fab = 1 - 0 = 1
        print("Theoretical error: ", e)
        print("Numeric error: ", abs(1-In))
        return In