from pylab import pi,sin
from MatrixSolve import Gauss
from numpy import zeros

class Exercise5:
    points = [(-pi, sin(-pi)),
              (-2.6, sin(-2.6)),
              (-1.3, sin(-1.3)),
              (-0.6, sin(-0.6)),
              (0,sin(0)),
              (0.5, sin(0.5)),
              (0.75, sin(0.75)),
              (1.7, sin(1.7)),
              (2.75, sin(2.75)),
              (pi,sin(pi))]

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
        n = len(self.points)
        a = zeros((n,1))
        dx = zeros((n-1,1))
        dy = zeros((n-1,1))

        for i in range(n-1):
            a[i] = self.points[i][1]
            dx[i] = self.points[i+1][0] - self.points[i][0]        
            dy[i] = self.points[i+1][1] - self.points[i][1]        

        A = zeros((n,n))
        A[0][0] = 1
        A[n-1][n-1] = 1
        r = zeros((n,1))

        for i in range(1,n-1):
            A[i][i-1] = dx[i-1]
            A[i][i] = 2*(dx[i-1] + dx[i])
            A[i][i+1] = dx[i]
            r[i] = 3*(dy[i]/dx[i] - dy[i-1]/dx[i-1])

        c = Gauss(A,r) # Solve for ci
        
        b = zeros((n-1,1))
        d = zeros((n-1,1))
        for i in range(n-1):
            d[i] = (c[i+1]-c[i])/(3*dx[i]) 
            b[i] = dy[i]/dx[i] - (dx[i]/3)*(2*c[i]+c[i+1])
        
        for i in range(n-1):
            if self.points[i][0]<x<self.points[i+1][0]:
                return a[i]+b[i]*(x-self.points[i][0]) + \
                       c[i]*(x-self.points[i][0])**2 + \
                       d[i]*(x-self.points[i][0])**3