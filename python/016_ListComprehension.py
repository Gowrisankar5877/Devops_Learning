lst = [i*i for i in range(1,10)]
print(lst)
lang = "Python"
lang = list(lang)
print(type(lang))
print(lang)

lst1 = [i for i in range(20)]
print(lst1)

lst4 = [(i,i*i) for i in range(5) ]
print(lst4)
print(lst4[0][0])

lst2 = [i for i in range(2,20,2)]
print(lst2)

lst3 = [i for i in range(1,20,2)]
print(lst3)

lst5 = [[1,2,3,4,5],[6,7],[8,9]]
lst6 = [number for row in lst5 for number in row]
print(lst6)

