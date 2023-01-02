import random
from pylab import pi,sin, plot,xlabel,ylabel,grid,show
from Askisi1 import Exercise1

def exercise1():
    exc = Exercise1()
    print(exc.lagrange(1))
    print(exc.points)
    print(exc.splines(1))
    print(exc.Msplines(1))
    print(exc.xi)
    print(exc.yi)
    x = [random.uniform(-3.14,3.14) for i in range(30)]
    x.sort()
    yl = [exc.lagrange(x[i]) for i in range(30)]
    ysp = [exc.splines(x[i]) for i in range(30)]
    ymsp = [exc.Msplines(x[i]) for i in range(30)]
    plot(x,yl)
    show()
    plot(x,ysp)
    show()
    plot(x,ymsp)
    show()

def main():
    exercise1()

main()