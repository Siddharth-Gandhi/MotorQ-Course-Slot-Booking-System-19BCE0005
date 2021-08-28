import student
import course


class University:
    def __init__(self, name):
        self.name = name
        self.student_list = {}  # key = student reg no, value = student object
        self.course_list = {}  # key = course code, value = course object

    def add_student(self, student):
        self.student_list[student.reg_no] = student

    def add_course(self, course):
        self.course_list[course.code] = course

    def drop_student(self, student):
        del self.student_list[student.reg_no]

    def drop_course(self, course):
        del self.course_list[course.code]

    def get_student_list(self):
        if len(self.student_list) == 0:
            print("No students registered yet")
            return
        for student_ in self.student_list.values():
            print(student_)

    def get_course_list(self):
        if len(self.course_list) == 0:
            print("No courses registered yet")
            return
        for course_ in self.course_list.values():
            print(course_)
