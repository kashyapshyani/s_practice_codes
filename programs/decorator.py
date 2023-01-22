# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
#             return

#         return func(a, b)
#     return inner

    
# @smart_divide
# def divide(a, b):
#     print(a/b)
    
# divide(2,5)

# smart_divide(3)

def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result

print(operate(inc,3))
print(operate(dec,3))