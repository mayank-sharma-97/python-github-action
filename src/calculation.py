def add(num1:int,num2:int) -> int:
    """add is function used to give the addition 
    of two inputted number

    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int: addition of num1 and num2
    """
    result = num1+num2 
    return result

def sub(num1:int,num2:int) -> int:
    """sub is function used to give the subtraction 
    of two inputted number

    if num1 is greater than num2 then returns num1 - num2
    
    else 

       num2 - num1

    Args:
        num1 (int): first number
        num2 (int): second number

    Returns:
        int: subtraction of inputted number
    """
    result = abs(num1-num2) 
    return result