from numpy import zeros,dot,transpose
from MatrixSolve import Gauss

def leastSquares2(points):
    n = len(points)
    A = zeros((n,3))
    b = zeros((n,1)) 
    for i in range(n):
        A[i][0] = 1
        A[i][1] = points[i][0]
        A[i][2] = points[i][0]**2
        b[i] = points[i][1]
        
    ATA = dot(transpose(A),A)
    ATb = dot(transpose(A),b)
    c = Gauss(ATA,ATb)
    return c

def leastSquares3Solve(x, points):
    c = leastSquares3(points)
    return c[0] + x * c[1] + c[2]*x**2 + c[3]*x**3

def leastSquares3(points):
    n = len(points)
    A = zeros((n,4))
    b = zeros((n,1)) 
    for i in range(n):
        A[i][0] = 1
        A[i][1] = points[i][0]
        A[i][2] = points[i][0]**2
        A[i][3] = points[i][0]**3
        b[i] = points[i][1]
        
    ATA = dot(transpose(A),A)
    ATb = dot(transpose(A),b)
    c = Gauss(ATA,ATb)
    return c

def leastSquares4(points):
    n = len(points)
    A = zeros((n,5))
    b = zeros((n,1)) 
    for i in range(n):
        A[i][0] = 1
        A[i][1] = points[i][0]
        A[i][2] = points[i][0]**2
        A[i][3] = points[i][0]**3
        A[i][4] = points[i][0]**4
        b[i] = points[i][1]
        
    ATA = dot(transpose(A),A)
    ATb = dot(transpose(A),b)
    c = Gauss(ATA,ATb)
    return c