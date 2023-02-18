from numpy import zeros, array, eye, copy, dot, sqrt


def Gauss_seidel(self):
    A = ([])
    b = ([])

    n = 10

    for i in range(n):
        A.append([])
        for j in range(n):
            if i == j:
                A[i].append(5.0)
            elif i == j + 1 or j == i + 1:
                A[i].append(-2.0)
            else:
                A[i].append(0.0)

    for i in range(n):
        if i == 0 or i == n - 1:
            b.append(3.0)
        else:
            b.append(1.0)

    x = ([])
    x.append([])
    for i in range(len(A)):
        x[0].append(0)

    k = 0
    while True:
        x.append([])
        for i in range(len(A)):
            x[k + 1].append(b[i])
            for j in range(1, i - 1):
                x[k + 1][i] -= A[i][j] * x[k + 1][j]
            for j in range(i + 1, len(A)):
                x[k + 1][i] -= A[i][j] * x[k][j]
            x[k + 1][i] /= A[i][i]

        if abs(max(x[k]) - max(x[k + 1])) <= self.wr:
            print(x[k])
            break

        k += 1

    def Cholesky(self, A):

        L = [[0.0 for x in range(len(A))] for y in range(len(A))]
        L = array(L)

        for k in range(len(A)):
            for i in range(len(A)):
                if k is not i:
                    L[k][i] += A[k][i]
                    for j in range(i-1):
                        L[k][i] -= L[i][j]*L[k][j]
                    if L[i][i] == 0:
                        L[k][i] = 0
                    else:
                        L[k][i] /= L[i][i]
                else:
                    L[k][k] += A[k][k]
                    for j in range(k-1):
                        L[k][k] -= pow(L[k][j], 2)
                    L[k][k] = sqrt(L[k][k])

        return L

