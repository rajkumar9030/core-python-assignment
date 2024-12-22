class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average_marks(self):
        return sum(self.marks) / len(self.marks)

def calculate_average(students):
    averages = {}
    for student in students:
        averages[student.name] = round(student.average_marks(), 2)
    return averages

def top_performer(students):
    top_student = max(students, key=lambda student: student.average_marks())
    return top_student.name

students_data = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

students = [Student(name, marks) for name, marks in students_data.items()]

averages = calculate_average(students)
top_student = top_performer(students)

print("Average Marks:", averages)
print("Top Performer:", top_student)
