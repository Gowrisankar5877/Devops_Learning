import re
string = "Good morning all, Kerala is good tod trivandrum is good our class is very good."
#match = re.search("all",string,re.I)
#match = re.match("all",string,re.I)
#match = re.findall("all",string,re.I)
#print(match)
"""if match:
    print("Matching",match.group(0))"""
match1 = re.findall("(?i)Morning",string)
#print(match1)
match2 = re.findall("good",string,re.I | re.DOTALL)
#print("Find all",match2)
match3 = re.search("good",string,re.I | re.DOTALL)
#print("Search",match3)
#myspan = match3.span()
#print(myspan)
l=[]
for i in re.finditer(re.escape("Good"),string,re.I):
    l.append(i.span())
    #print(i)
#print(l)
match4 = re.sub("(?i)Good","Awesome",string)
#print(match4)


string1 = '''Hi 
Hello
Welcome'''
match5 = re.split("\n",string1)
#print(match5)

pattern = r'[l].[m]'
match6 = re.findall(pattern,string)
print(match6)

