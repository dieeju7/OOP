class DirectoryEntry:
    def __init__(self, identifier, name):
        self._id = identifier # Initialize identifier attribute
        self._name = name # Initialize name attribute

    def id(self):
        return self._id

    def name(self):
        return self._name

# Class representing a course, inheriting from DirectoryEntry
class Course(DirectoryEntry):
    def __init__(self, course_id, name, start_time, end_time):
        super().__init__(course_id, name) # Call parent class constructor with course_id and name
        self._start_time = start_time # Initialize start_time attribute
        self._end_time = end_time  # Initialize end_time attribute

    def start_time(self):
        return self._start_time

    def end_time(self):
        return self._end_time

class CourseDirectory:
    def __init__(self):
        self._courses = {}
    # add course function
    def add_course(self, course_id, name, start_time, end_time):
        if course_id not in self._courses:
            self._courses[course_id] = Course(course_id, name, start_time, end_time)
    # search course function
    def search_course(self, query):
        found_courses = []
        for course in self._courses.values():
            if query.lower() in course.name().lower() or query == course.id():
                found_courses.append(course)
        if found_courses:
           # return "\n".join([f"ID: {course.id()}, Name: {course.name()}, Start Time: {course.start_time()}, End Time: {course.end_time()}" for course in found_courses])
            return found_courses[0]
        else:
            return None
            #return "Course not found"
