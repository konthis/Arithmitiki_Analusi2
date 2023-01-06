from LeastSquares import *
from numpy import polyfit, poly1d
from pylab import plot, show


class Exercise7:

    # bday 5/5

    # Technology index closes (ASE)
    DTX = [2315.99,   # 19/4
           2319.55,   # 20/4
           2329.25,   # 21/4
           2299.51,   # 26/4
           2221.23,   # 27/4
           2256.81,   # 28/4
           2249.2,    # 29/4
           2153.66,   #  3/5
           2152.46,   #  4/5
           2065.76]   #  5/5
    
    # Energy index closes (ASE)
    DPA = [3823.09,   # 19/4
           3870.41,   # 20/4
           3830.82,   # 21/4
           3864.31,   # 26/4
           3822.67,   # 27/4
           3871.8,    # 28/4
           3854.22,   # 29/4
           3751.24,   #  3/5
           3790.35,   #  4/5
           3851.0601] #  5/5
    
    pointsDTX = [(-6,2315.99),
                 (-5,2319.55),
                 (-4,2329.25),
                 (1,2299.51),
                 (2,2221.23),
                 (3,2256.81),
                 (4,2249.2),
                 (8,2153.66),
                 (9,2152.46),
                 (10,2065.76)]

    pointsDPA = [(-6,3823.09),
                 (-5,3870.41),
                 (-4,3830.82),
                 (1,3864.31),
                 (2,3822.67),
                 (3,3871.8),
                 (4,3854.22),
                 (8,3751.24),
                 (9,3790.35),
                 (10,3851.0601)]

    predictionsIndexes = [11,  #6/5  1 close after 5/5
                          17,] #12/5 5 closes after 5/5

    actualPredictedCloses = [(11, 3813,55),
                             (17, 3916,22)]

    def solvePolynom(self, c, x):
        for i in range(5-len(c)):
            c = list(c)
            c.append(0)
        return c[0] + x*c[1] + c[2]*x**2+\
               c[3]*x**3 + c[4]*x**4

    def calculateCoeffs(self):
        return leastSquares2(self.pointsDTX),\
               leastSquares3(self.pointsDTX),\
               leastSquares4(self.pointsDTX),\
               leastSquares2(self.pointsDPA),\
               leastSquares3(self.pointsDPA),\
               leastSquares4(self.pointsDPA)

    def predictions(self):
        x = [point[0] for point in self.pointsDPA]

        c2DTX, c3DTX, c4DTX, c2DPA, c3DPA, c4DPA = self.calculateCoeffs() 
        print("\tDTX")
        print("2nd degree: ")
        print("- 6/5 prediction", self.solvePolynom(c2DTX, 
                                 self.predictionsIndexes[0]))
        print("- 12/5 prediction", self.solvePolynom(c2DTX, 
                                 self.predictionsIndexes[1]))

        print("3rd degree: ")
        print("- 6/5 prediction", self.solvePolynom(c3DTX, 
                                 self.predictionsIndexes[0]))
        print("- 12/5 prediction", self.solvePolynom(c3DTX, 
                                 self.predictionsIndexes[1]))

        print("4th degree: ")
        print("- 6/5 prediction", self.solvePolynom(c4DTX, 
                                 self.predictionsIndexes[0]))
        print("- 12/5 prediction", self.solvePolynom(c4DTX, 
                                 self.predictionsIndexes[1]))

        print("\tDPA")
        print("2nd degree: ")
        print("- 6/5 prediction", self.solvePolynom(c2DPA, 
                                 self.predictionsIndexes[0]))
        print("- 12/5 prediction", self.solvePolynom(c2DPA, 
                                 self.predictionsIndexes[1]))

        print("3rd degree: ")
        print("- 6/5 prediction", self.solvePolynom(c3DPA, 
                                 self.predictionsIndexes[0]))
        print("- 12/5 prediction", self.solvePolynom(c3DPA, 
                                 self.predictionsIndexes[1]))

        print("4th degree: ")
        print("- 6/5 prediction", self.solvePolynom(c4DPA, 
                                 self.predictionsIndexes[0]))
        print("- 12/5 prediction", self.solvePolynom(c4DPA, 
                                 self.predictionsIndexes[1]))

        y2DTX = [self.solvePolynom(c2DTX, p[0]) for p in self.pointsDTX]
        y2DPA = [self.solvePolynom(c2DPA, p[0]) for p in self.pointsDPA]
        y3DTX = [self.solvePolynom(c3DTX, p[0]) for p in self.pointsDTX]
        y3DPA = [self.solvePolynom(c3DPA, p[0]) for p in self.pointsDPA]
        y4DTX = [self.solvePolynom(c4DTX, p[0]) for p in self.pointsDTX]
        y4DPA = [self.solvePolynom(c4DPA, p[0]) for p in self.pointsDPA]
        
        plot(x, y2DPA, 'r')
        plot(x, y3DPA, 'g')
        plot(x, y4DPA, 'b')
        show()
        plot(x, y2DTX, 'r')
        plot(x, y3DTX, 'g')
        plot(x, y4DTX, 'b')
        show()