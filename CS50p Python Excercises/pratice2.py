def main():
    grades = {"Sarah": 92, "John": 88, "Emma": 75}
    name = input("Enter student's name: ")
    person(grades, name)

def person(grades,name):
    if name in grades:
        print(f"{name}'s grade is {grades[name]}")
    else:
        print("Student not found")







main()
