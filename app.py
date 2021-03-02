"""Function to raise power recursively"""
def raise_power(base,exp):

    """Base Cases"""
    """Checks to see if exp==0"""
    if(exp == 0):
        return 1

    """Checks to see if exp==1"""
    if(exp == 1):
        """Returns base of any num raise to 1 equals num itself"""
        return(base)

    """Recursive Case"""
    """Checks to see if exp is not equal to one"""
    if(exp != 1):

        """Mulitiply base recursively by the function"""
        return(base * raise_power(base, exp-1))

"""Prints result after function is complete"""
print(raise_power(8,2))


