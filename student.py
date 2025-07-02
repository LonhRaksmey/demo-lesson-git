class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Create students
students = []

def add_student(name, age, grade):
    student = Student(name, age, grade)
    students.append(student)
    print(f"Added {name} to the system")

def show_all_students():
    print("\n--- All Students ---")
    for student in students:
        student.display()

def find_student(name):
    for student in students:
        if student.name.lower() == name.lower():
            return student
    return None

# Demo
add_student("Alice", 16, 10)
add_student("Bob", 17, 11)
add_student("Carol", 15, 9)

show_all_students()

# Find a student
found = find_student("Alice")
if found:
    print(f"\nFound student: {found.name}")
else:
    print("Student not found")