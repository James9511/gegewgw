courses = ["MIT", "Cybersecurity", "Datascience"]

print(courses)

# Accessing an element in an array
print(courses[1])

# Looping through an array
for courses in courses:
    print(courses)

# Adding a new element in an array
courses.append("Android Programming")
print(courses)

# Deleting an element from an array
courses.remove("Datascience")
print(courses)
