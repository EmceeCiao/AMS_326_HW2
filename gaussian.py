import numpy as np  

def gaussian_elimination(N): 
    """ 
    Function to perform gaussian elimination on Ax=b, where A is N x N and 
    b is N x 1 and is all ones. 

    Inputs: 
    - N: Size of N * N matrix to be randomly generated 
    Outputs: 
    - x: A vector of size N that is the solution to Ax = b 
    
    """
    A = np.random.uniform(low=-1, high=1, size=(N, N))  
    b = np.ones((N,1)) 
    Ab = np.hstack((A,b)) # Concatenates A and b

    for i in range(N):  
        max_val = 0 
        max_row = i
        for row in range(i, N): 
            # We only care to change this if it's a higher absolute max value  
            if(abs(Ab[row][i])) > max_val: 
                max_val = abs(Ab[row][i]) 
                max_row = row 
        if i != max_row:   
            # Numpy Row Swapping Below! 
            Ab[[i, max_row]] = Ab[[max_row, i]] 
    
        # Now we can actually start eliminating below our max row 
        # which starts at i+1 and goes to N
        for row in range(i+1, N): 
            factor = Ab[row, i]/Ab[i, i] 
            Ab[row, i:] -= factor * Ab[i, i:]   

    # Now Ab is in upper triangular form, so we backsubstitute to 
    # solve our system of equations  

    x = np.zeros(N) # initalize x to 0's
    for i in range(N-1, -1, -1):  # N - 1 is our last row! 
        # Sum of all other known-values plugged in  
        non_target_x_vals = np.sum(Ab[i, i+1:N] * x[i+1 : N]) 
        # Solving the unknown x by solving coeff * x + knowns = b
        x[i] = (Ab[i, -1] - non_target_x_vals)/(Ab[i, i])
    
    # Validation Check and Answer Printed Below! 
    x_np = np.linalg.solve(A,b)  
    print(f"Answer from Numpy's to Double Check:")  
    print(x_np.flatten()) 
    print(f"\n")
    print(f"Answer from our implementation:\n") 
    print(x)
    return x 

x = gaussian_elimination(66)  
print("")
