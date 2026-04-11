import json

json_str = '{"name" : "Abc", "age": 24}'

print(json_str)
print(type(json_str))

py_obj = json.loads(json_str)

print(py_obj)
print(type(py_obj))

py_obj1 = {
    "name": "Def",
    "age": 24
}

json_str1 = json.dumps(py_obj1)

print(json_str1)
print(type(json_str1))

# with open("data.json", "r") as f:
#     data = json.load(f)
#     print(data)


py_obj2 = {
    "name" : "Abc2", 
    "age": 26 
}

with open("data.json", "w") as f:
    json.dump(py_obj2, f, indent=4, sort_keys=True)
