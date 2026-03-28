s = {1,2,3,2,1}

print(s)
print(type(s))
print(len(s))

s.add(5)

print(s)

empty_dict = {}

print(type(empty_dict), empty_dict)
empty_set = set()
print(type(empty_set), empty_set)

s.remove(5)
print(s)
# s.pop()
# print(s.pop())
# s.clear()
print(s)

s1 = {1,2,3,4,5}
s2 = {2,4,6}

print(s1.union(s2))
print(s1.intersection(s2))



info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]


courses_set = set()
english_course_names = []
dict = {}

for name, course in info:
    courses_set.add(course)
    if(course == "English"):
        english_course_names.append(name)
    
    if(dict.get(name) == None):
        dict.update({name: set()})
    
    dict[name].add(course)

print(courses_set)
print(english_course_names)
print(dict)