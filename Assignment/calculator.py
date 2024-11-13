def add(a,b):
    return a+b

def difference(a,b):
    return a-b


def product(a,b):
    return a*b

def divition(a,b):
    if b==0:
        return ZeroDivisionError("division by zero is not possible")
    else:
        return (a/b)
    

