# import re
# file = input("Enter the file path")
# f = open(file)
# #print(f.readlines())
# #pattern = "[a-zA-Z0-9._%+-" "]+@[a-zA-Z0-9.-]+.[a-zA-Z]"
# #pattern = '[a-zA-Z0-9._%+-]+@gmail+.com' 
# #pattern = "[\\w._]+@[\\w]*+.[\\w]*"
# pattern='[\\w\.-]+@[\\w\.-]+\\.\\w+'
# l=[]
# for i in f.readlines():
#     #print("output of i",i)
#     match = re.findall(pattern,i)
#     if match:
#         l.append(match)
#         #print(match)
# print(l)
import re
def extract_emails(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        emails = re.findall(r'[\w._+-]+@[\w.-]+\.[a-zA-Z]{2,}', content)
        return emails       
file_path = "C:/Users/Administrator/Devops/Devops_Learning/python/gowri.txt"  
emails = extract_emails(file_path)
print("Extracted Emails:")
for email in emails:
        print(email)    
extract_emails(file_path)