# Day 3 - Dictionaries Practice

# 1. Create a dictionary
student = {
    "name": "Surya",
    "age": 20,
    "city": "Vijayawada",
    "course": "Computer Science"
}
print("Student info:", student)

# 2. Access values
print("\nName:", student["name"])
print("City:", student.get("city"))
print("Grade (default):", student.get("grade", "Not assigned"))

# 3. Add and update entries
student["grade"] = "A"
student["age"] = 21
print("\nUpdated student:", student)

# 4. Delete an entry
del student["course"]
print("After deletion:", student)

# 5. Iterate over dictionary
print("\nAll keys and values:")
for key, value in student.items():
    print(f"  {key}: {value}")

# 6. Dictionary with list values
marks = {
    "math": [85, 90, 78],
    "physics": [72, 88, 91],
    "python": [95, 98, 100]
}
print("\nSubject averages:")
for subject, scores in marks.items():
    avg = sum(scores) / len(scores)
    print(f"  {subject}: {avg:.1f}")

# 7. Count word frequency using dict
sentence = "to be or not to be that is the question to ask"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print("\nWord frequency:", word_count)

# 8. Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print("\nSquares dict:", squares_dict)
