# Create
students = { 
    "name": ["john", "jane", ["Sam", "Luck"]],
    "age": "12",
    "gender": "m",
    "courses": {
        "level_1": {
            "sem_1": [],
            "sem_2": []
        }, 
        "level_2": {
            "sem_1": ["English", "Maths", "Akan"],
            "sem_2": []
        }, 
    }

}

persons = [
    {
        "name": "John",
        "age": "12",
        "gender": "m"
    },
    {
        "name": "Mina",
        "age": "10",
        "gender": "f"
    },
    {
        "name": "Jane",
        "age": "15",
        "gender": "f"
    }
]

persons = {
    "John": {
        "username": "",
        "name": "John",
        "age": "12",
        "gender": "m"
    }
}


names = ["john", "jane"]

# access 
# print(students['name'][2][0])
# print(students["courses"]["level_2"]["sem_1"])
if "grade" in students:
    print(students["grade"])



# change
students["age"] = "15"

names[0] = "Sandra"

# print(names)

# add 
students["key"] = "new"


# remove
popped = students.pop("key")
students["key"] = ""
print(students)


