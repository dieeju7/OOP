from student import Student, StudentDirectory
from course import Course, CourseDirectory
from kurssi import Classes

def main():
    studentdirectory = StudentDirectory()
    coursedirectory = CourseDirectory()
    class_list = []

    while True:
        print("Commands:")
        print("0 - Exit")
        print("1 - Add student")
        print("2 - Search student")
        print("3 - Add course")
        print("4 - Search course")
        print("5 - Create class")
        print("6 - Add student to class")
        print("7 - Add course to class")
        print("8 - Search student in class")
        command = input("Command: ")
 
        if command == "0":
            break
 
        elif command == "1":
            student_id = input("Student ID: ")
            name = input("Name: ")
            studentdirectory.add_student(student_id, name)
            print("Student added.")
 
        elif command == "2":
            query = input("Enter student ID or name: ")
            result = studentdirectory.search_student(query)
            if result == None:
                print("Can't find the student")
            else:
                print(f'Student {result.name()} has beed added')

        elif command == "3":
            course_id = input("Course ID: ")
            name = input("Name: ")
            start_time = input("Start Time: ")
            end_time = input("End Time: ")
            coursedirectory.add_course(course_id, name, start_time, end_time)
            print("Course added.")

        elif command == "4":
            query = input("Enter course ID or name: ")
            result = coursedirectory.search_course(query)
            if result == None:
                print("Can't find the student")
            else:
                print(f'Course {result.name()} has beed added')

        elif command == "5":
            name = input("Class name: ")
            schedule = input("Schedule: ")
            new_class = Classes(name, schedule)
            class_list.append(new_class)
            print("Class created.")

        elif command == "6":
            class_name = input("Class name: ")
            student_name = input("Student name: ")
            # check student availble or not
            student_obj = studentdirectory.search_student(student_name)
            if not student_obj:
                print("Student not found")
                continue
            class_found = False
            for class_obj in class_list:
                if class_obj.name == class_name:
                    student_obj = studentdirectory.search_student(student_name)
                    if student_obj:
                        class_obj.add_student_to_class(student_obj)
                        print(f"Added {student_name} to {class_name}")
                        class_found = True
                        break
            if not class_found:
                print("Class not found.")

        elif command == "7":
            class_name = input("Class name: ")
            course_name = input("Course name: ")
            for class_obj in class_list:
                if class_obj.name == class_name:
                    course_obj = coursedirectory.search_course(course_name)
                    if course_obj:
                        class_obj.add_course_to_class(course_obj)
                        print(f"Added {course_name} to {class_name}")
                    else:
                        print("Course not found.")
                    break
            else:
                print("Class not found.")

        elif command == "8":
            class_name = input("Class name: ")
            student_name = input("Student name: ")
            for class_obj in class_list:
                if class_obj.name == class_name:
                    result = class_obj.search_student(student_name)
                    print(result)
                    break
            else:
                print("Class not found.")

        else:
            print("Invalid command. Please try again.")
 

if __name__ == "__main__":
    main()