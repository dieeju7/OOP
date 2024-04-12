class Student:
    def __init__(self, student_id, name):
        self._id = student_id
        self._name = name
 
    def id(self):
        return self._id
 
    def name(self):
        return self._name
 
class StudentDirectory:
    def __init__(self):
        self._students = {}
 
    def add_student(self, student_id, name):
        if student_id not in self._students:
            self._students[student_id] = Student(student_id, name)
 
    def search_student(self, query):
        found_students = []
        for student in self._students.values():
            if query.lower() in student.name().lower() or query == student.id():
                found_students.append(student)
        if found_students:
            ##return "\n".join([f"ID: {student.id()}, Name: {student.name()}" for student in found_students])
            return found_students[0]
        else:
            return None
