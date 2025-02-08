#findout which is the character repating the most
llist=[1,2,3,4,5,6,1,1,2,2,3,4,5,1,2,4,1,4]
llist=["a","b","c","d","a","a","a","b","c","d","e","b","b","b","e","a"]
distinct_list = list(set(llist))
count = 0
for i in distinct_list:
    ccount=llist.count(i)
    if ccount > count:
        count=ccount
        character = i
print(character)
