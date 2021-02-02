def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    msg = None
    if a > b:
        msg = "First is greater"
    elif b > a:
        msg = "Second is greater"
    elif a == b:
        msg = "Numbers are equal"
    else:
        msg = "a and b both have to be numbers"
    return msg