import random
from pylab import pi,sin, plot,xlabel,ylabel,grid,show
from Askisi1 import Exercise1

def exercise1():
    exc = Exercise1()
    x = [random.uniform(-3.14,3.14) for i in range(200)]
    x.sort()
    ysin = [sin(xi) for xi in x]
    ylagrange = [exc.lagrange(xi) for xi in x]
    yDiffLagrange = [ysin[i]-ylagrange[i] for i in range(200)]
    ysplines = [exc.splines(xi) for xi in x]
    yDiffSplines = [ysin[i]-ysplines[i] for i in range(200)]
    yleastSquares = [exc.leastSquares(xi) for xi in x]
    yDiffLeastSquares = [ysin[i]-yleastSquares[i] for i in range(200)]
    plot(x,yDiffLagrange,'r')
    plot(x,yDiffSplines,'m')
    plot(x,yDiffLeastSquares,'b')
    show()
    #ylg = [exc.lagrange(x[i]) for i in range(30)]
    #ysp = [exc.splines(x[i]) for i in range(30)]
    #yls = [exc.leastSquares(x[i]) for i in range(30)]
    #plot(x, ylg, 'r')
    #plot(x, ysp, 'm')
    #plot(x, yls, 'g')
    #show()

def main():
    exercise1()

main()