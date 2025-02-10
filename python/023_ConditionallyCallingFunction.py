def square(x):
    return x**2
def cube(x):
    return x**3
def abs(x):
    if x >= 0:
        return x
    else:
        return -(x)
def Hof(type):
    if type=="square":
        return square
    elif type =="cube":
        return cube
    elif type=="abs":
        return abs
    else:
        return "No Function mentioned"
    
var=Hof("square")
print(var(4))