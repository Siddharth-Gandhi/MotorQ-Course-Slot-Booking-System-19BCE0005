# How to run:

```
    python registration.py
```

or

```
    python3 registration.py
```

# Requirements

- [ ] check for slot clashes, and warn in CLI

- [x] CLI interface, maybe web if time permits (no web interface yet)

- [x] class -> subject, capacity, time slot, registered_students[]: student, waiting_queue[] : student

- [x] student -> roll_no, registered_class[]: class, unregister_class()

 <!-- [] college -> courses_offered[], students[] -->

- [x] registration -> classes_offered[] : class, students[] : student, opening_time, closing_time

- [x] maintain waiting queue, if a student in that class leaves, first from queue is added to the registered

- [x] list of classes, students

- [x] university object to keep track of both students and courses

- [x] create and upload to github
