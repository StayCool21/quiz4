from dataclasses import dataclass

@dataclass
class Student:
    name:str
    id:int
    age:int

def main():
    students = [
        Student("Joey", 0, 18),
        Student("Luke", 1, 19),
        Student("Billy", 2, 20)
    ]
    students.append(Student("Ray", 3, 19))

    print(students[1])

    oldest_student = max(students, key=lambda p:p.age)
    print(f"The oldest student is {oldest_student.age}")

    students[2].name = "Ray"
    print(f"Student 2's new name is {students[2].name}")

if __name__ == '__main__':
    main()