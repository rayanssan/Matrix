from copy import deepcopy
from time import process_time

class Matrix:
    """Methods for operations with matrices."""
    
    def __init__(self, matrix):
        """
        Initializes and instance of the Matrix class

        Requires: matrix to be a list of lists with elements of the type int or float.
        Ensures: initializing the given matrix as an attribute on the Matrix class.
        """
        self._matrix = deepcopy(matrix)

    def getMatrix(self) -> list:
        """Returns the self._matrix attribute."""
        return self._matrix

    def setMatrix(self, newMatrix):
        """
        Sets the self._matrix attribute equal to a new matrix attribute.

        Requires: newMatrix to be a list of lists with elements of the type int or float.
        Ensures: setting self._matrix equal to newMatrix.
        """
        self._matrix = newMatrix

    def add(self, matrixB):
        """
        Adds two matrices of the same size.

        Requires: matrixB to be an object of the Matrix class.
        Ensures: returning the matrix resulting from the addition
        of the currently initialized matrix with matrixB.
        """
        matrixA = self.getMatrix()
        rows = len(matrixA)
        cols = len(matrixA[0])
        
        result = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(matrixA[i][j] + matrixB.getMatrix()[i][j])
            result.append(row)
        
        return result


    def matrixProduct(self, matrixB) -> list:
        """
        Multiplies the currently initialized matrix with another matrix stored in a Matrix object.
        
        Requires: matrixB to be an object of the Matrix class.
        Ensures: returning the matrix resulting from the multiplication
        of the currently initialized matrix with matrixB.
        """
        matrixA = self.getMatrix()
        matrixB = matrixB.getMatrix()
        # Check if matrices can be multiplied
        if len(matrixA[0]) != len(matrixB):
            raise ValueError("Matrices cannot be multiplied. \
            Number of rows of B must equal the number of columns of A.")
            
        # Initialize the resulting matrix with zeros
        result = [[0.0 for j in range(len(matrixB[0]))] for i in range(len(matrixA))]
        
        # Multiply the matrices
        for i in range(len(matrixA)):
            for j in range(len(matrixB[0])):
                for k in range(len(matrixB)):
                    result[i][j] += matrixA[i][k] * matrixB[k][j]
        return result

    def isInverse(self, matrixB) -> bool:
        """
        Determines whether or not a given matrixB≠I is inverse of the currently initialized matrix.
        
        Requires: the initialized matrix to be a square matrix;
        matrixB to be an object of the Matrix class;
        matrixB to be different from the identity matrix.
        Ensures: returning True if matrixB is inverse of the currently initialized matrix, 
        otherwise returning False.
        """
        # if AB = BA then A and B are inverses of each other
        productAB = self.matrixProduct(matrixB)
        productBA = matrixB.matrixProduct(self)

        return productAB == productBA
        

    def determinant(self) -> int or float:
        """
        Calculates the determinant of a given matrix, and returns this value as an int.
        
        Requires: the initialized matrix to be a square matrix nxn with 0 <= n <= 10.
        """
        matrix = self.getMatrix()
        n = len(matrix)
		
        # setting base cases: if empty matrix and zero matrix
        if n == 0 or matrix == [[]]:
            return 0
		# if non-square matrix return message
        if n != len(matrix[0]):
            return "Non-square matrices do not have determinants"
        # elif 1x1 matrix return the single element
        elif n == 1:
            return matrix[0][0]
        # elif 2x2 matrix return the simple cross multiplication of elements
        elif n == 2:
            return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
        # elif nxn, n>2, apply laplace expansion
        else:
            # Â(i,j) = (-1)**(i+j)detA(i|j)
            # det(A) = a(1,1)*Â(1,1) + a(1,2)*Â(1,2) + ... + a(n,n)*Â(n,n)
            det = 0
            for j in range(n):
                submatrix = Matrix([[matrix[i][k] for k in range(n) if k != j] for i in range(1, n)])
                det += matrix[0][j] * ((-1) ** j) * submatrix.determinant()
            return det

    def transpose(self) -> list:
        """
        Returns the transpose of a matrix.
        """
        matrix = self.getMatrix()
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        transposeMatrix = [[0 for x in range(rows)] for x in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                transposeMatrix[j][i] = matrix[i][j]
        
        return transposeMatrix

    def rowEchelon(self) -> list:
        """
        Reduces a matrix to reduced row echelon form.
        """
        matrix = self.getMatrix()
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        lead = 0
        
        for r in range(rows):
            if lead >= cols:
                return matrix
            
            # find the first row below the current row with a non-zero lead
            i = r
            while matrix[i][lead] == 0:
                i += 1
                if i == rows:
                    i = r
                    lead += 1
                    if cols == lead:
                        return matrix
            
            # swap the rows if necessary
            if i != r:
                matrix[r], matrix[i] = matrix[i], matrix[r]
            
            # normalize the current row by dividing by the leading entry
            leadingEntry = matrix[r][lead]
            matrix[r] = [entry / float(leadingEntry)  if entry != 0 else 0.0 for entry in matrix[r]]
            
            # eliminate the leading entry in all rows below the current row
            for i in range(rows):
                if i != r:
                    leadingEntry = matrix[i][lead]
                    matrix[i] = [entryCol - leadingEntry*entryRow for 
                    entryRow, entryCol in zip(matrix[r], matrix[i])]
            
            lead += 1
        
        return matrix

    def __str__(self) -> str:
        """Returns a string representation of the matrix attribute stored in the Matrix class."""
        return f'A = {self.getMatrix()}'

    def __eq__(self, otherMatrix) -> bool:
        """
        Handles equality comparisons of objects of the Matrix class.

        Requires: otherMatrix to be an object of the Matrix class.
        Ensures: sucessful equality comparisons between objects of the Matrix class.
        """
        return self.getMatrix() == otherMatrix

    def __lt__(self, otherMatrix) -> bool:
        """
        Handles less than comparisons of objects of the Matrix class.

        Requires: otherMatrix to be an object of the Matrix class.
        Ensures: sucessful less than comparisons between objects of the Matrix class.
        """
        return self.getMatrix() == otherMatrix


#-------------Example Usage - Determinant of an 8x8 identity matrix-------------
    
start = process_time()

A = [[1,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,1]]

print(f'det(A) = {Matrix(A).determinant()}')
    
print(f'elapsed time: {process_time()-start}')