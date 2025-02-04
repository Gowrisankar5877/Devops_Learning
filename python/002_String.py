multi_line_string = '''I am Devops Engineer at UST. 
I am looking forward to grow in the organization in 5 years and experience different roles '''
print(multi_line_string)
Fname = "Gowri Sankar"
Lname = "Marepalli"
print("name is", Fname+" "+Lname)
print(len(Fname+" "+Lname))
string="I am Devops Engineer at UST. \n I am looking forward to grow in the organization in 5 years and experience different roles. \tEnjoy Life"
print(string)
print(string[0])
print(string[0:5])
print(string[0:8:2])
print(string[::-1])
print(string[-8:-1:1])
for i in string:
    print(i,end=" ")
for i in range(len(string)):
    print(string[i])
print(string.count("I"))
print(string.endswith("Life"))
print("index",string.find("i"))
print(string.expandtabs(10))
print(string.rfind("i"))
print(string.index('i', 11))
print(string.rindex("i" ))
string="hihow123"
print(string.isalnum())
print(string.isalpha())
print(string.isnumeric())
s3 = "\u00b2"
print(s3.isdecimal())
print(s3.isdigit())
s4="24"
print(s4.isdecimal())
var = "123"
print(var.isidentifier())
s5 = "lower upper"
print(s5.lower())
print(s5.upper())
a = ["Hi","Hello", "Who are you"]
print(" ".join(a))
print(s5.strip("e"))
print(s5.split(" "))
print(s5.title())
print(s5.capitalize())
print(s5.swapcase())
print(s5.replace("lower","upper"))
print(s5.startswith("low"))

