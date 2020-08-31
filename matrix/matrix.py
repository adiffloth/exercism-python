class Matrix:

    def __init__(self, matrix_string):
        self.rows = matrix_string.split('\n')

    def row(self, index):
        return list(map(int, self.rows[index-1].split()))

    def column(self, index):
        col = []
        for row in self.rows:
            col.append(int(row.split()[index-1]))
        return col
