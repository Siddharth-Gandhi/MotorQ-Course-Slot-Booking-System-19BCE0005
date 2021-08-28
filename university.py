import student
import course


class University:
    def __init__(self, name):
        self.name = name
        self.student_list = {}  # key = student reg no, value = student object
        self.course_list = {}  # key = course code, value = course object

    def add_student(self, student):
        self.student_list[student.reg_no] = student
        print(f"{student} has been registered")

    def add_course(self, course):
        self.course_list[course.course_code] = course
        print(f"{course} has been registered")

    def drop_student(self, student):
        del self.student_list[student.reg_no]
        print(f"{student} has been removed from {self.name}")

    def drop_course(self, course):
        del self.course_list[course.course_code]
        print(f"{course} has been removed from {self.name}")

    def get_student_list(self):
        print(f"\nList of students registered in {self.name}:")
        if len(self.student_list) == 0:
            print("No students registered yet")
            return
        for srno, student_ in enumerate(self.student_list.values()):
            print(f"\t {srno+1}. {student_}")
        print("\n")

    def get_course_list(self):
        print(f"\nList of courses registered in {self.name}:")
        if len(self.course_list) == 0:
            print("No courses registered yet")
            return
        for srno, course_ in enumerate(self.course_list.values()):
            print(f"\t {srno+1}. {course_}")
        print("\n")
