info = [
    ("Aman", "Python"),
    ("Aman", "Java"),
    
    ("Riya", "C++"),
    ("Riya", "Web Development"),
    
    ("Karan", "Data Science"),
    ("Aman", "Data Science"),
    
    ("Neha", "Machine Learning")
]
# Print all the unique courses
# s = set()
# for tup in info:
#     s.add(tup[1])

# print(s)






# print all the students which are inrolled in data science

# for tup in info:
#     if(tup[1]=="Data Science"):
#         print(tup[0])



# create a dictionary (studens, set of courses)

dict = {}

for name, courses in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(courses)
    else:
        dict[name].add(courses)
print(dict)