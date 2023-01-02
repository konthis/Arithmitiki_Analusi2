from pylab import pi,sin, plot,xlabel,ylabel,grid,show
import random
import numpy

class Exercise1:
    
    points = [(-pi, sin(-pi)),(-3.1, sin(-3.1)),(-2.6, sin(-2.6)),(-1.3, sin(-1.3)),
             (0.75, sin(0.75)),(0,sin(0)),(0.5, sin(0.5)),(1.7, sin(1.7)),(2.75, sin(2.75)),(pi,sin(pi))]

    xi = [i for i,j in points]
    yi = [j for i,j in points]

    def graph(self):
        x = [i[0] for i in self.points]
        y = [i[1] for i in self.points]
        plot(x,y)
        xlabel('x')
        ylabel('y')
        grid(True)
        show()
        
    def Li(self,i, x):
        n = len(self.points) # total points
        result = 1
        for j in range(n):
            if j==i:
                continue
            result *= (x-self.points[j][0])/(self.points[i][0]-self.points[j][0])
        return result

    def lagrange(self, x):
        n = len(self.points)
        result = 0
        for i in range(n):
            result += self.points[i][1]*self.Li(i,x)
        return result
    
    def splines(self, x):
        n = len(self.points) - 1
        a = [0.]*(n-1)
        b = [0.]*n
        d = [0.]*n
        h = [self.points[i+1][0] - self.points[i][0]  for i in range(n)]
        c = [0.]*(n+1)
        l = [0.]*(n+1)
        u = [0.]*(n+1)
        z = [0.]*(n+1)
        for i in range(1,n-1):
            a[i] = (3./h[i])*(self.points[i+1][1]-self.points[i][1]) - (3./h[i-1])*(self.points[i][1] - self.points[i-1][1])

        l[0] = 1.
        l[n] = 1.
        for i in range(1,n-1):
            l[i] = 2.*(self.points[i+1][0]-self.points[i-1][0])-h[i-1]*u[i-1]
            z[i] = (a[i]-h[i-1]*z[i-1])/l[i]
        
        for i in range(n-2,-1,-1):
            c[i] = z[i] - u[i]*c[i+1]
            b[i] = (self.points[i+1][1] - self.points[i][1])/h[i] - h[i]*(c[i+1] + 2*c[i])/3.
            d[i] = (c[i+1]-c[i])/(3.*h[i])

        for i in range(n):
            if(self.points[i][0]<x<self.points[i+1][0]):
                return self.points[i][1] + b[i] * x + c[i] * pow(x, 2) + d[i] * pow(x, 3)
            

        

    def Msplines(self, x):
        hi = []
        for i in range(len(self.xi) - 1):
            hi.append(self.xi[i + 1] - self.xi[i])

        q1 = []
        for i in range(len(self.yi) - 1):
            q1.append((3 * (
                    self.yi[i + 1] * hi[i - 1] - self.yi[i] * (self.xi[i + 1] - self.xi[i - 1]) + self.yi[i - 1] *
                    hi[i])) / (hi[i-1]*hi[i]))

        l = []
        u = []
        z = []

        l.append(1)
        u.append(0)
        z.append(0)

        for i in range(1, len(self.xi) - 1):
            l.append(2 * (self.xi[i + 1] - self.xi[i - 1]) - hi[i - 1] * u[i - 1])
            u.append(hi[i] / l[i])
            z.append((q1[i] - hi[i - 1] * z[i - 1]) / l[i])

        l.append(1)
        z.append(0)

        c = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
        b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        d = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        for j in range(1, len(self.xi)):
            i = len(self.xi) - 1 - j
            c[i] = z[i] - (u[i] * c[i + 1])
            b[i] = ((self.yi[i + 1] - self.yi[i]) / hi[i]) - ((hi[i] * (c[i + 1] + (2 * c[i]))) / 3)
            d[i] = (c[i + 1] - c[i]) / (3 * hi[i])

        #print("A")
        #print(q1)
        #print("b")
        #print(b)
        #print("d")
        #print(c)
        #print("c")
        #print(d)
        #print("h")
        #print(hi)
        #print("l")
        #print(l)
        #print("U")
        #print(u)
        #print("z")
        #print(z)
        for i in range(len(self.xi) - 1):
            if self.xi[i] < x < self.xi[i + 1]:
                return self.yi[i] + b[i] * x + c[i] * pow(x, 2) + d[i] * pow(x, 3)






        
        

