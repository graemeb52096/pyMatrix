__author__ = 'BatesG1996'


class Matrix:
    """
    This class represents a mathematical matrix.

    """
    def get(self, index):
        """
        Get a specific entry, row or col. from matrix
        >>> A = [[1,2,3],[4,5,6],[7,8,9]]
        >>> matrix_A = Matrix(A)
        >>> matrix_A.get((1,1))
        1
        >>> matrix_A.get((1,None))
        [1,2,3]
        >>> matrix_A.get((None,1))
        [1,4,7]


        :param index: Index of element
         :type index: Tuple
        :return: Matrix entry
        """
        # Get column
        if index[0] is None:
            # Create a temporary list to hold our output values
            temp_list = []
            # Get column index
            col = index[1] - 1
            # Append column element from row to temp list
            for row in self.values:
                temp_list.append(row[col])
            # Return temp
            return temp_list

        # Get row
        elif index[1] is None:
            # Get row index
            row = index[0] - 1
            # Return row
            return self.values[row]
        # Get entry
        else:
            # For user ease, row and col start at 1,1 instead of 0,0
            row = index[0] - 1
            col = index[1] - 1
            # Return entry at index.
            return (self.values[row])[col]

    def set(self, index, value):
        """
        Set specific entry in matrix.

        :param index: Index of element ex. (1,2)
         :type index: Tuple
        :param value: New value of element
        :return: None
        """

        # Set column
        if index[0] is None:
            # Get column index
            col = index[1] - 1
            # Append column element from row to temp list
            i = 0
            for row in self.values:
                (row[col]) = value[i]
                i += 1

        # Set row
        elif index[1] is None:
            # Get row index
            row = index[0] - 1
            # Set row
            self.values[row] = value
        # Set entry
        else:
            # For user ease, row and col start at 1,1 instead of 0,0
            row = index[0] - 1
            col = index[1] - 1
            # Set entry at index.
            (self.values[row])[col] = value

    def transpose(self):
        # Get the number of columns
        num_cols = self.size[1]
        # Create a temporary list to hold new rows
        new_rows = []
        # Add each column to new rows list
        for x in range(1, num_cols+1):
            new_rows.append(self.get((None, x)))
        # Return the transposed Matrix
        return Matrix(new_rows)

    def __str__(self):
        """

        :return: Matrix in string form
        """
        temp_str = ''
        for row in self.values:
            for col in row:
                temp_str += ' %s' % col
            temp_str += '\n'
        return temp_str

    def __init__(self, values):
        """
        :param values: Values to populate the matrix. List of Lists, each list represents a row.
         :type values: List of Lists
        """
        self.values = values
        self.size = (len(values), len(values[0]))


class SquareMatrix(Matrix):
    """

    """

    def get_diagonal(self):
        """
        """
        # Get number of rows/cols
        rows = self.size[0]
        cols = self.size[1]
        # Create a list to hold diagonal values
        diagonal = []
        # Get each diagonal entry
        for r in range(0, rows):
            for c in range(0, cols):
                if r == c:
                    entry = (self.values[r])[c]
                    diagonal.append(entry)
        # Return diagonal list
        return diagonal

    def set_diagonal(self, values):
        """
        """
        # Get number of rows/cols
        rows = self.size[0]
        cols = self.size[1]
        # Set each value of diagonal with given values
        for r in range(0, rows):
            for c in range(0, cols):
                if r == c:
                    (self.values[r])[c] = values[r]

    def __init__(self, values):
        Matrix.__init__(self, values)


class IdentityMatrix(SquareMatrix):
    """

    """

    def __init__(self, value, size):
        # Create values list
        values = []
        # Create identity based on given size
        for x in range(0, size):
            # Create rows based on given size
            row = []
            # Add columns based on given size
            for i in range(0, size):
                # If column lies on diagonal add identity values
                if x == i:
                    row.append(value)
                # Else set entry to zeros
                else:
                    row.append(0)
            # Add row to values list
            values.append(row)
        # Initialize SquareMatrix with identity matrix values.
        SquareMatrix.__init__(self, values)


class MirroredMatrix(SquareMatrix):
    """

    """

    def set(self, index, value):
        """
        Sets value for both index and its mirror.

        :param index:
        :param value:
        :return:
        """

        pass

    def __init__(self, values):
        SquareMatrix.__init__(self, values)
        pass


def add_matrices(A, B):
    """
    Adds two matrices A,B

    :param A: Matrix A
    :param B: Matrix B
    :return: Matrix A+B
    """

    pass


def subtract_matrices(A, B):
    """

    :param A: Matrix A
    :param B: Matrix B
    :return: Matrix A+B
    """

    pass