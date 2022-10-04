import numpy as np

def solve_system_eq(X, y):
    """
    This function will take a Matrix X and its corresponding y vector as inputs and return the solution of the system of equations. 
    Note X and y should be numpy arrays. Muhammad Ali Faraz 10/03/2022
    """
    #Get in verse of X 
    # X . b  = y
    # b = X_inv . y
    y_ = np.array(y)
    X_ = np.array(X)
    if X_.shape[1] == y_.shape[0]:
        print("Dimension check passed")
        inverse_X = np.linalg.inv(X_)
        return np.dot(inverse_X, y_)
    else:
        print("Dim mismatch")
        return 0


#Driver
def driver(M = [[2,3],[5,4]], y = [2,3] ):
    """
    call this function to test  solve_system_eq function. Default values for M and y are defined but you can pass you own.
    """
    print(solve_system_eq(M,y))

driver([[2,3],[5,4]], [1,9])