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

def add(num1,num2):
    res=num1+num2
    return res
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
print(add(num1,num2))

person = {"Firstname":"Gowri Sankar", 
          "Last Name":"Marepalli", 
          "UID":290445,
          "friends":["Gowri", "sam"],
          "skills":{
              "backend_skills":["Python","Java"],
               "frontend skills" : ["HTML","CSS"]
          }}
