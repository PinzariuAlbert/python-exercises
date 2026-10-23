import json

names = ["Anna", "Sam", "Mia"]
grade = {
    "name":"sam",
    "grade":5
}

with open("names.txt", "w") as file:
    json.dump(grade, file)
    
with open("names.txt", "r") as file:
    grades_from_file = json.load(file)
    print(grades_from_file["name"])