# Matrix

The Matrix class provides a collection of methods for performing various operations on matrices. 
It is designed to handle matrices represented as lists of lists containing integer or 
floating-point numbers.

- Initialization:

  - `__init__(self, matrix: object) -> None`:
  Initializes an instance of the Matrix class.
  Requires matrix to be a list of lists with elements of type int or float.
  Deep copies the given matrix to ensure encapsulation.

- Methods:

  - `getMatrix(self) -> list`:
  Returns the matrix stored in the Matrix instance.

  - `setMatrix(self, newMatrix: object) -> None`:
  Sets the matrix attribute to a new matrix.
  Requires newMatrix to be a list of lists with elements of type int or float.

  - `add(self, matrixB: object) -> None`:
  Adds two matrices of the same size.
  Requires matrixB to be another Matrix object.
  Returns the resulting matrix from the addition.

  - `matrixProduct(self, matrixB: object) -> list`:
  Multiplies the current matrix with another matrix stored in a Matrix object.
  Requires matrixB to be another Matrix object.
  Ensures the matrices are compatible for multiplication.
  Returns the resulting matrix from the multiplication.
  
  - `isInverse(self, matrixB: object) -> bool`:
  Determines whether the given matrixB is the inverse of the current matrix.
  Requires both matrices to be square and matrixB to be another Matrix object.
  Returns True if matrixB is the inverse, otherwise returns False.

  - `determinant(self) -> int or float`:
  Calculates the determinant of the matrix.
  Requires the matrix to be a square matrix of size nxn where 0 <= n <= 10.
  Returns the determinant value.

  - `transpose(self) -> list`:
  Returns the transpose of the matrix.

  - `rowEchelon(self) -> list`:
  Reduces the matrix to its row echelon form.
  Returns the resulting row echelon matrix.

  - `__str__(self) -> str`:
  Provides a string representation of the matrix.
  Useful for easy visualization of the matrix contents.

  - `__eq__(self, otherMatrix: object) -> bool`:
  Handles equality comparisons between Matrix objects.
  Requires otherMatrix to be another Matrix object.
  Returns True if the matrices are equal, otherwise False.

  - `__lt__(self, otherMatrix: object) -> bool`:
  Handles less-than comparisons between Matrix objects.
  Requires otherMatrix to be another Matrix object.
  Returns True if the current matrix is less than the otherMatrix, otherwise False.
