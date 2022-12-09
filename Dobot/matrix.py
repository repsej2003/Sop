
class matrix:
    def __init__(self, rows, cols, matrix=None):
        self.rows = rows
        self.cols = cols
        if matrix is None:
            self.data = [[0 for _ in range(cols)]for _ in range(rows)]
        else:
            self.data = matrix

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


if __name__ == "__main__":
   # m1 = matrix(2, 2, [[1, 0], [1, 2]])
    # m1.print()
   # print("")

    m2 = matrix(2, 3, [[1, 3, 5], [2, 4, 6]])
    m2.print()

    ans = m2.transpose()
    ans.print()
  #  print("")
    #ans = m1 * m2
    # ans.print()
