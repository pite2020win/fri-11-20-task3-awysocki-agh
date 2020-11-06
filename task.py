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
