person = {"Firstname":"Gowri Sankar", 
          "Last Name":"Marepalli", 
          "UID":290445,
          "friends":["Gowri", "sam"],
          "skills":{
              "backend_skills":["Python","Java"],
               "frontend skills" : ["HTML","CSS"]
          }}
print(len(person))
print(person.get("skills").get("backend_skills"))
person["address"]="Trivandrum"
print(person.get("address"))
print(person)
print("address" in person)
print(person.pop("address"))
print(len(person))
del person["friends"]
print(person["skills"]["backend_skills"].append("C"))
print(person["skills"]["backend_skills"])
print(person.items())
person_copy = person.copy()
del person
print(person_copy)
keys=person_copy.keys()
for i in keys:
    print(i)
    print(person_copy[i])
