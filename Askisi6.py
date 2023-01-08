from numpy import pi,sin

class Exercise6:

    a = 0
    b = pi/2
    n = 10

    def calculateFx(self):
    # n is number of parabols and NOT amount of points
        x = [self.a+i*(self.b-self.a)/self.n for i in range(self.n+1)] 
        y = [self.f(xi) for xi in x]
        return y

    def f(self,x): return sin(x)

    def simpson(self):
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
        print("Simpson's rule: \n")
        print("Actual value: 1.")
        print("Approximated value: %.6f"%In)
        print("Theoretical error: %.6f"%e)
        print("Numeric error: %.6f"%abs(1-In), "\n")

        return In
    
    def trapezoidRule(self):
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
        print("Trapezoid rule: \n")
        print("Actual value: 1.")
        print("Approximated value: %.6f"%In)
        print("Theoretical error: %.6f"%e)
        print("Numeric error: %.6f"%abs(1-In),"\n")
        return In