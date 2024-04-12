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
           # return "\n".join([f"ID: {course.id()}, Name: {course.name()}, Start Time: {course.start_time()}, End Time: {course.end_time()}" for course in found_courses])
            return found_courses[0]
        else:
            return None
            #return "Course not found"