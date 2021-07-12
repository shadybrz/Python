class Matrix:
    def __init__(self, matrix_string):
        row = matrix_string.split("\n")
        self.matrix = [[int(col) for col in row.split()] for row in row]

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]