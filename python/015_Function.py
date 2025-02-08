def Hello_World(msg):
    print(msg)
msg = input("Enter the message")
Hello_World(msg)

def add(num1,num2):
    res=num1+num2
    return res
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
print(add(num1,num2))

def list_num(l):
    for i in l:
        print(i)
l=list(map(int,input("Enter list of numbers").split(" ")))
list_num(l)

def check_prime(num):
    flag = 1
    for i in range(2, int(n**0.5)+1):
        if num%i==0:
            flag =0
            break
    if flag==1:
        return "Prime Number"
    else:
        return "Not a prime Number"
n=int(input("Enter the number you want to check whether prime or not"))
print(check_prime(n))

def first_repeating_element(l):
    another_list = []
    for i in l:
        if i in another_list:
            return i
        else:
            another_list.append(i)

l=list(map(int,input("Enter elements to search repeating elements").split(" ")))
print(first_repeating_element(l))