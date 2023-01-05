from numpy import zeros,array, eye, copy, dot

def Gauss_Seidel(A, b, tol):
            size = len(A)
            x = zeros((2,size))
            while True:
                for i in range(size):
                    x[1][i] = (b[i] - \
                        sum([A[i][j]*x[1][j] for j in range(i-1)]) - \
                        sum([A[i][j]*x[0][j] for j in range(i+1,size)]))/A[i][i]
                if abs(max(x[1] - x[0])) <= tol:
                    return x[1]
                x[0] = x[1]