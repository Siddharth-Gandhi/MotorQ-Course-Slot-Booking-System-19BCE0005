import course


class Student:
    def __init__(self, name=None, reg_no=None):
        self.name = name
        self.reg_no = reg_no  # primary keys
        self.registered_courses = {}  # key = course code and value = course object

    def __str__(self):
        return f"{self.name} ({self.reg_no})"

    def register(self, new_course):
        """Register a course for the student"""

        # TODO: check timeslot clashes

        if new_course.course_code in self.registered_courses:
            # already registered
            print(f"{new_course.course_name} is already registered")
            return
        # try to register in course
        if new_course.register_student(self):
            self.registered_courses[new_course.course_code] = new_course
            print(f"{new_course.course_name} registered for {self}")
        else:
            print("Course capacity full")

    def unregister(self, cur_course):
        """Unregister a course from the student"""
        if cur_course.course_code in self.registered_courses:
            # remove from student's list
            del self.registered_courses[cur_course.course_code]
            # remove from course's list
            cur_course.drop_student(self)
            print(f"{cur_course.course_name} unregistered for {self}")
