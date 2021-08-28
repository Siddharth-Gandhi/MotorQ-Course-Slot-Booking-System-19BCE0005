import university
import student
import course

if __name__ == "__main__":
    print("Welcome to the Course Slot Booking System by 19BCE0005 Siddharth Gandhi \n")

    vit = university.University("VIT Vellore")
    registration_open = False

    while True:
        var = input('\n ...press enter to open registration...')
        if not(var):
            registration_open = True
            print("Registrations OPEN!\n")
            break
        else:
            print('Press enter to open registration')

    main_menu = "\n" + "Please select an option from the following:" + "\n\n" + \
        "***** Main MENU *****" + "\n" + \
        "1. Enroll a new student" + "\n" + \
        "2. Create a new course" + "\n" + \
        "3. List all students" + "\n" + \
        "4. List all courses" + "\n" + \
        "5. Register a student for a course" + "\n" + \
        "6. Unregister a student for a course" + "\n" + \
        "7. List registered students for a course" + "\n" + \
        "8. End registration" + "\n" + \
        "9. EXIT" + "\n"

    while registration_open:
        while True:
            var = input('\n Press enter to open main menu')
            if not(var):
                break
            else:
                print('Press enter to open main menu')
        print(main_menu)
        print('<' + '-'*24 + '\n')
        option = int(input("Enter your option: "))
        if option == 1:
            student_name = input("Enter student name: ")
            student_roll = input("Enter student roll number: ")
            student_obj = student.Student(student_name, student_roll)
            vit.add_student(student_obj)
        elif option == 2:
            course_code = input("Enter course code: ")
            course_name = input("Enter course name: ")
            timeslot = input("Enter timeslot: ")
            max_capacity = int(input("Enter maximum capacity: "))
            course_obj = course.Course(
                course_name, course_code, timeslot, max_capacity)
            vit.add_course(course_obj)
        elif option == 3:
            vit.get_student_list()
        elif option == 4:
            vit.get_course_list()
        elif option == 5:
            vit.get_course_list()
            vit.get_student_list()
            student_roll = input("Enter student roll number: ")
            course_code = input("Enter course code: ")
            if student_roll in vit.student_list and course_code in vit.course_list:
                vit.student_list[student_roll].register(
                    vit.course_list[course_code])
            else:
                print("Student not found or course not found")
        elif option == 6:
            vit.get_course_list()
            vit.get_student_list()
            student_roll = input("Enter student roll number: ")
            course_code = input("Enter course code: ")
            if student_roll in vit.student_list and course_code in vit.course_list:
                vit.student_list[student_roll].unregister(
                    vit.course_list[course_code])
            else:
                print("Student not found or course not found")
        elif option == 7:
            if len(vit.course_list) > 0:
                vit.get_course_list()
                course_code = input("Enter course code: ")
                if course_code in vit.course_list:
                    vit.course_list[course_code].list_registered_students()
                else:
                    print("Course not found")
            else:
                print("No courses registered yet")
        elif option == 8:
            registration_open = False
        elif option == 9:
            break
        else:
            print("Invalid option")
        print('-'*24 + '>' + '\n')
