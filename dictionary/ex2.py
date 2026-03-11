# Creating a dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA",
    "marks": 85
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key
student["college"] = "SNPSU"

# Updating value
student["marks"] = 90

# Printing full dictionary
print("Updated Dictionary:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)