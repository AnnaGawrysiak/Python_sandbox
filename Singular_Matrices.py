import numpy as np

A = np.array([
        [9, 7, -5, 3],
        [2, 8, 0, 4],
        [3, 12, 0, 5],
        [1, 3, 1, 3]
    ], dtype=np.float_)

def isSingular(A):

    B = np.array(A, dtype = np.float_)
    try:
        fixRowZero(B)
        fixRowOne(B)
        fixRowTwo(B)
        fixRowThree(B)
    except MatrixIsSingular:
        return True
    return False

# This next line defines our error flag. For when things go wrong if the matrix is singular.
# There is no need to edit this line.
class MatrixIsSingular(Exception): pass

def fixRowZero(A):
    if A[0][0] == 0:
        A[0][0] = A[0][0] + A[1][0]
    if A[0, 0] == 0:
        A[0] = A[0] + A[2]
    if A[0, 0] == 0:
        A[0] = A[0] + A[3]
    if A[0, 0] == 0:
        raise MatrixIsSingular()
    A[0] = A[0] / A[0, 0]
    return A

def fixRowOne(A):
    # First we'll set the sub-diagonal elements to zero, i.e. A[1,0].
    A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        A[1] = A[1] + A[2]
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        A[1] = A[1] + A[3]
        A[1] = A[1] - A[1, 0] * A[0]
    if A[1, 1] == 0:
        raise MatrixIsSingular()
    A[1] = A[1] / A[1, 1]
    return A

def fixRowTwo(A) :
    # Setting the sub-diagonal elements of row two to zero (there are two of them).
    A[2] = A[2] - A[2, 0] * A[0]
    A[2] = A[2] - A[2, 1] * A[1]

    # testing if the diagonal element is not zero.
    if A[2, 2] == 0:
        A[2] = A[2] + A[3]
        A[2] = A[2] - A[2, 0] * A[0]
        A[2] = A[2] - A[2, 1] * A[1]
    if A[2, 2] == 0:
        raise MatrixIsSingular()
    # Finally set the diagonal element to one by dividing the whole row by that element.
    A[2] = A[2] / A[2, 2]
    return A

def fixRowThree(A) :

    A[3] = A[3] - A[3][0]*A[0]
    A[3] = A[3] - A[3][1]*A[1]
    A[3] = A[3] - A[3][2]*A[2]

    if(A[3][3] == 0):
        raise MatrixIsSingular

    A[3] = A[3]/A[3][3]

    return A
