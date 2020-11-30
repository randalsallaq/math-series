
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))  
print(fibonacci(10))


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1    
    else:
        return (lucas(n-1) + lucas(n-2))
print(lucas(9))

def sum_series(n, base1=0, base2=1):
    # if (base1 !==0 and base2 !==1) or (base1 !== 2 and base2 !== 1):
    #     return n
    if base1 == 0 and base2 == 1:
        return fibonacci(n)

    elif base1 == 2 and base2 == 1:
        return lucas(n)    




         
            
    
