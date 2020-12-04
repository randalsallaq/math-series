
def fibonacci(n):
    """ 
    Fibunacci is a mathmatical series where each number is the sum of the two preceding ones, starting from 0 and 1.
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))  
print(fibonacci(8))




def lucas(n):
    """ 
    Lucas is a mathmatical series where each number is the sum of the two preceding ones, starting from 2 and 1.
    """
    if n == 0:
        return 2
    if n == 1:
        return 1    
    else:
        return (lucas(n-1) + lucas(n-2))
print(lucas(9))




def sum_series(n, base1=0, base2=1):
    """
    in this function we are passing 3 parameters, the first one determines which math series will be executed; fibunacci or lucas
    """

    # if (base1 !==0 and base2 !==1) or (base1 !== 2 and base2 !== 1):
    #     return n
    if base1 == 0 and base2 == 1:
        return fibonacci(n)

    elif base1 == 2 and base2 == 1:
        return lucas(n)    




         
            
    
