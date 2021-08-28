import queue
import datetime

import student


class Course:
    def __init__(self, course_name=None, course_code=None, timeslot=None, max_capacity=0):
        self.course_name = course_name
        self.max_capacity = max_capacity
        self.course_code = course_code  # primary key
        self.timeslot = timeslot
        # self.registered_students = set()
        self.registered_students = {}  # key = student reg no and value = student object
        self.waiting_list = queue.Queue()
        self.capacity = 0

    def __str__(self):
        return (f"Subject: {self.course_name}({self.course_code}); Capacity: {self.max_capacity}; Timings: {self.timeslot}")

    def register_student(self, new_student):
        if new_student.reg_no in self.registered_students:
            print(f"{new_student} is already registered for {self.course_name}")
            return
        if self.capacity < self.max_capacity:
            self.registered_students[new_student.reg_no] = new_student
            print(
                f"{new_student} has been successfully registered for {self.course_name}")
            self.capacity += 1
            return True
        else:
            self.waiting_list.put(new_student)
            print(
                f"Class is at maximum capacity, {new_student} is added to {self.course_name}'s waiting list")
            return False

    def register_from_waiting_list(self):
        if self.waiting_list.empty():
            print("Waiting list is empty")
            return
        self.register_student(self.waiting_list.get())

    def drop_student(self, cur_student):
        # assuming a valid student is passed in
        if cur_student.reg_no in self.registered_students:
            # remove from registered
            # self.registered_students.remove(cur_student)
            del self.registered_students[cur_student.reg_no]
            print(f"{cur_student.name} has been removed from {self.course_name}")
            self.capacity -= 1
            # register the first student in waiting list
            self.register_from_waiting_list()
        else:
            print(f"{cur_student} is not registered for {self.course_name}")

    def list_registered_students(self):
        print(
            f"\n{self.course_name} has {self.capacity}/{self.max_capacity} students registered:")

        for srno, student_ in enumerate(self.registered_students.values()):
            print(f"\t {srno+1}. {student_}")
        print("\n")
