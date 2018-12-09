import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    # Taking the exponential of every number
    expL = np.exp(L)
    # Summing all the exponentials
    sumExpL = sum(expL)
    result = []
    # Dividing exponential of every number 
    # by the sum of all exponentials
    for i in expL:
        result.append((i*1.0)/sumExpL)
        
    #returning the result as a list
    return result

    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())