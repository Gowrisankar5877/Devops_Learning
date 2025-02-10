def  sum(a,b):
    return a+b
print(sum(2,4))

mysum = lambda a,b : a+b
print(mysum(2,4))

print((lambda a,b: a+b) (2,3))

#Example orf lambda frunction in other function
def power(x):
    return lambda n: x**n
print(power(4)(2))