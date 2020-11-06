#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

class Matrix:
    def __init__(self, *vals):
        self.mtx = []
        self.mtx.append([vals[0], vals[1]])
        self.mtx.append([vals[2], vals[3]])

    def __str__(self):
        return str(self.mtx)

    def __add__(self, o):
        if isinstance(o, Matrix):
            m = Matrix(self.mtx[0][0] + o.mtx[0][0], self.mtx[0][1] + o.mtx[0][1], self.mtx[1][0] + o.mtx[1][0], self.mtx[1][1] + o.mtx[1][1])
            return m
        if isinstance(o, int) or isinstance(o, float):
            m = Matrix(self.mtx[0][0] + o, self.mtx[0][1] + o, self.mtx[1][0] + o, self.mtx[1][1] + o)
            return m
    
        return None

    def __matmul__(self, o):
        if isinstance(o, Matrix):
            m = Matrix(self.mtx[0][0] * o.mtx[0][0] + self.mtx[0][1] * o.mtx[1][0],
                       self.mtx[0][1] * o.mtx[0][0] + self.mtx[0][1] * o.mtx[1][0],
                       0, 0)
            return m 
        return None


if __name__ == '__main__':
    matrix_1 = Matrix(4.,5.,6.,7.)
    matrix_2 = Matrix(2.,2.,2.,1.)


    matrix_4 = matrix_2 + matrix_1
    print(matrix_4)

    matrix_4 = matrix_1 + 6
    print(matrix_4)

    matrix_3 = matrix_2 @ matrix_1
    print(matrix_3)
