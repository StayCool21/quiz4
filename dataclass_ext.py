from dataclasses import dataclass

@dataclass
class Student:
    name:str
    id:int
    age:int

    def __init__(self, name:str, id:int, age:int) -> None:
        self.name = name
        self.id = id
        self.age = age

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."

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

   # use the __str__ method
    print(students[0])

if __name__ == '__main__':
    main()