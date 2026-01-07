skills = ["JavaScript", "HTML", "CSS"]

print("My skills:", skills)
print("First skill:", skills[0])

skills.append("Python")

print("Updated skills:", skills)



student = {
    "name": "Nadeem",
    "age": 22,
    "goal": "Remote GenAI Developer"
}
print("Student name:", student["name"])
print("Student goal:", student["goal"])

print("Skills are:")
for skill in skills:
    print("-", skill)


students = [
    {"name": "Nadeem","skill": "JavaScript"},
    {"name": "Sara","skill": "Python"},
    {"name": "Ali","skill": "HTML"}
]

print("Student List:")

for student in students:
    print(student["name"], "knows",student["skill"])

