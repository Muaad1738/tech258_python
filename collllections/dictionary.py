# dictionary

student1 = {
    "name" : "suasan",
    "stream" : "tech",
    "completed_lessons": 4,
    "completed_lessons_naames": ["variables", "data types", "set_up", "collections"],
}

print(student1["stream"])
print(student1["completed_lessons_naames"][0])
student1["completed_lessons"] = 3
print(student1["completed_lessons"])
student1["completed_lessons_naames"]. remove("collections")
print(student1["completed_lessons_naames"])

print(type(student1.keys()))


