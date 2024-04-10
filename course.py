class Course:
    def __init__(self, course_id, name, start_time, end_time):
        self._id = course_id
        self._name = name
        self._start_time = start_time
        self._end_time = end_time

    def id(self):
        return self._id

    def name(self):
        return self._name

    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time


class CourseDirectory:
    def __init__(self):
        self._courses = {}

    def add_course(self, course_id, name, start_time, end_time):
        if course_id not in self._courses:
            self._courses[course_id] = Course(course_id, name, start_time, end_time)

    def search_course(self, query):
        found_courses = []
        for course in self._courses.values():
            if query.lower() in course.name().lower() or query == course.id():
                found_courses.append(course)
        if found_courses:
            return "\n".join([f"ID: {course.id()}, Name: {course.name()}, Start Time: {course.start_time()}, End Time: {course.end_time()}" for course in found_courses])
        else:
            return "Course not found"


def main():
    directory = CourseDirectory()
    while True:
        print("Commands:")
        print("0 - Exit")
        print("1 - Add course")
        print("2 - Search course")
        command = input("Command: ")

        if command == "0":
            break

        elif command == "1":
            course_id = input("Course ID: ")
            name = input("Name: ")
            start_time = input("Start Time: ")
            end_time = input("End Time: ")
            directory.add_course(course_id, name, start_time, end_time)
            print("Course added.")

        elif command == "2":
            query = input("Enter course ID or name: ")
            result = directory.search_course(query)
            print(result)

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
