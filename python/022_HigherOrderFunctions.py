def sum_numbers(x):
    return sum(x)

def HigherOrderFunction(f,lst):
    summation = f(lst)
    return summation
result = HigherOrderFunction(sum_numbers,[1,2,3,4,5])
print(result)