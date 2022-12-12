from math import radians, cos, sin


class matrix:
    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.data = [[0 for _ in range(cols)]for _ in range(rows)]
        else:
            if not isinstance(matrix, list) or not isinstance(matrix[0], list):
                raise Exception("Matrix must be a 2d list")
            self.data = matrix
            self.rows = len(matrix)
            self.cols = len(matrix[0])

    def __mul__(self, other):
        if self.cols != other.rows:
            raise Exception(
                "The first matrix must have the same numbers of coloms as the other has rows")
        m = matrix(self.rows, other.cols)
        for row in range(self.rows):
            for col in range(other.cols):
                vec1 = self.data[row]
                vec2 = [other.data[i][col] for i in range(other.rows)]
                dotproduct = sum(vec1[i] * vec2[i] for i in range(self.cols))
                m.data[row][col] = dotproduct

        return m

    def invert(self):
        pass

    def transpose(self):
        return matrix(self.cols, self.rows, [[self.data[row][col] for row in range(self.rows)] for col in range(self.cols)])

    def print(self):
        for row in range(self.rows):
            string = ""
            for col in range(self.cols):
                string += f'{self.data[row][col]} '
            print(string)

    @classmethod
    def Identity(cls, size):
        m = matrix(size, size)
        for i in range(size):
            m.data[i][i] = 1

        return m

    # fixed angels X-Y-Z in degeress
    @classmethod
    def tranformation(cls, gamma, beta, alpha, x, y, z):
        gamma = radians(gamma)
        beta = radians(beta)
        alpha = radians(alpha)
        data = [[cos(alpha)*cos(beta), cos(alpha)*sin(beta)*sin(gamma)-sin(alpha)*cos(gamma), cos(alpha)*sin(beta)*cos(gamma)+sin(alpha)*cos(gamma), x],
                [sin(alpha)*cos(beta), sin(alpha)*sin(beta)*sin(gamma)+cos(alpha)*cos(gamma), sin(alpha)*sin(beta)*cos(gamma)-cos(alpha)*sin(gamma), y],
                [-sin(beta), cos(beta)*sin(gamma), cos(beta)*cos(gamma), z],
                [0, 0, 0, 1]
                ]
        return matrix(4, 4, [[round(data[x][y], 4) for y in range(4)] for x in range(4)])


if __name__ == "__main__":
    m1 = matrix(3, 2, [[1, 3], [1, 5]])
    m1.print()
    print("")

    m2 = matrix.Identity(2)
    m2.print()
    print("")

    ans = m1 * m2
    ans.print()
    matrix.Identity(10)
    matrix.tranformation(-90, 0, 0, 10, 15, 20).print()
