info = {
    "name": "Abc",
    "name": "Def",
    "age": 25,
    "courses": ["Math", "Physics"],
    3.14: "PI"
}

info["age"] = 27
print(info)
print(type(info))
print(info.keys())
print(list(info.keys()))
print(type(list(info.keys())))
print(list(info.values()))
print(info.items())
print(list(info.items()))
print(info.get("age"))
print(info.get("age2"))
# print(info["age2"])

info.update({
    "gender": "MALE"
})

print(info)