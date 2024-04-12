from student import Student
from course import Course

class Classes():
    def __init__(self,name, schedule):
        self.name = name
        self.schedule = schedule
        self.student_list = []

    def __str__(self):
        return f"{self.name}: has join. Here is the student list {self.student_list} "
    
    def add_student_to_class(self,student: Student):
        self.student_list.append(student)
    
    def add_course_to_class(self,course: Course):
        self.student_list.append(course)

    def search_student(self,name):
        for student in self.student_list:
            if name == student.name():
                return f"{name} in the class list "
        return f"can't not find {name} in the class list"  
