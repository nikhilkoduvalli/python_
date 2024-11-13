# #swap function

# def swap_num(fn):
#     def wrapper(a,b):
#         if a<b:
#             a,b=b,a
#         return fn(a,b)
#     return wrapper

# @swap_num
# def subtract(a,b):
#     return a-b

# print(subtract(5,7)) 


# @swap_num
# def division(a,b):
#     return a/b
# print(division(3,6))









""" wap to create functions addition, subtraction, divison, multiplication, modulus, floor
division
values,
# in these functions use decorators for avoiding getting negative and fractioned

"""

def swap_num(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap


# @swap_num
# def math_op(a,b):
#     print(f"Sum={a+b}")
#     print(f"difference={a-b}")
#     print(f"Product={a*b}")
#     print(f"Subtraction={a/b}")

# math_op(4,3)



"""# wap a function to division which return a/b, need to check if a<b then swap
# use another decorator for check b=0, if b==0 return a message to the unction that
"not possible"""



def swap_num(func):
    def wrap(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return wrap

def cheque(fun):
    def che(a,b):
        if b!=0:
            return fun(a,b)
        else:
            return print("not possible")
            
    return che
@swap_num
@cheque
def divis(a,b):
    print(a/b)
divis(6,0)




