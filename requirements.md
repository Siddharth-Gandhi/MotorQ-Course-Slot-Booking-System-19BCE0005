- [ ] CLI interface, maybe web if time permits

[x] class -> subject, capacity, time slot, registered_students[]: student, waiting_queue[] : student

[x] student -> roll_no, registered_class[]: class, unregister_class()

 <!-- [] college -> courses_offered[], students[] -->

[x] registration -> classes_offered[] : class, students[] : student, opening_time, closing_time

[] check for slot clashes, and warn in CLI

[x] maintain waiting queue, if a student in that class leaves, first from queue is added to the registered

[x] list of classes

[x] university object to keep track of both students and courses
