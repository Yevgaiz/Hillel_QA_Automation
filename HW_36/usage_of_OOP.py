from datetime import date, timedelta

""" Абстрактный класс Person """


class Person:
    def __init__(self, person_id, name, surname):
        self._person_id = person_id
        self._name = name
        self._surname = surname

    def get_person_id(self):
        return self._person_id

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def display_info(self):
        raise NotImplementedError("Subclasses should implement this!")


""" Класс наследующий от Person """


class Instructor(Person):
    def __init__(self, person_id, name, surname, years_of_experience):
        super().__init__(person_id, name, surname)
        self.years_of_experience = years_of_experience

    def display_info(self):
        return f"Name: {self._name}, Surname: {self._surname}, ID: {self._person_id}, Experience: {self.years_of_experience} years"


""" Класс наследующий от Person """


class Student(Person):
    def __init__(self, person_id, name, surname):
        super().__init__(person_id, name, surname)

    def display_info(self):
        return f"Name: {self._name}, Surname: {self._surname}, ID: {self._person_id}"


"""Ассоциация с CourseAssignment и Instructor"""


class Course:
    def __init__(self, course_code, title, description, duration):
        self._course_code = course_code
        self.title = title
        self.duration = duration
        self.description = description

    def get_course_code(self):
        return self._course_code

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_duration(self):
        return self.duration

    def display_info(self):
        return f"Course [Code: {self._course_code}, Title: {self.title}, Description: {self.description}, Duration: {self.duration} weeks]"


"""Класс ITCourse, агрегирующий Course"""


class ITCourse:
    def __init__(self, course):
        self._course = course
        self._students = []
        self._instructor = None

    def assign_instructor(self, instructor):
        self._instructor = instructor

    def add_students(self, *students):
        for student in students:
            self._students.append(student)

    def get_course(self):
        return self._course

    def get_instructor(self):
        return self._instructor

    def get_students(self):
        return self._students

    def display_info(self):
        instructor_info = self._instructor.display_info() if self._instructor else "No instructor assigned"
        students_info = [student.display_info() for student in self._students]
        return f"ITCourse [{self._course.display_info()}]\nInstructor: {instructor_info}\nStudents: {', '.join(students_info)}"


"""Класс Grade, зависимый от Student и Course"""


class Grade:
    def __init__(self, student, course, score, date_assigned):
        self._student = student
        self._course = course
        self._score = score
        self._date_assigned = date_assigned

    def get_student(self):
        return self._student

    def get_course(self):
        return self._course

    def get_score(self):
        return self._score

    def get_date_assigned(self):
        return self._date_assigned

    def display_info(self):
        return (f"Grade [Student: {self._student.get_name()} {self._student.get_surname()}, "
                f"Course: {self._course.get_title()}, Score: {self._score}, Date Assigned: {self._date_assigned}]")


"""Ассоциация с Course и Instructor"""


class CourseAssignment:
    def __init__(self, assignment_id, course, instructor, assignment_date):
        self._assignment_id = assignment_id
        self._course = course
        self._instructor = instructor
        self._assignment_date = assignment_date
        self._duration = course.get_duration()
        self._end_date = assignment_date + timedelta(weeks=self._duration)

    def display_info(self):
        return (
            f"CourseAssignment [ID: {self._assignment_id}, Course: {self._course.get_title()}, Instructor: {self._instructor.get_name()} {self._instructor.get_surname()}, "
            f"Assignment Date: {self._assignment_date}, End date: {self._end_date}]")


course1 = Course("QA123", "QA Automation Python", "Опануй автоматизоване тестування на Python!", 16)

it_course1 = ITCourse(course1)

instructor1 = Instructor(12345, "Oleksii", "Lytvynov", 15)
student1 = Student(223421, "Kostiantyn", "Pshenyshniuk")
student2 = Student(321234, "Kateryna", "Ilnytska")
student3 = Student(321235, "Yevhenll", "Alzenberg")
student4 = Student(321236, "Taras", "Andrusiv")
student5 = Student(321237, "Darla", "Veresha")

it_course1.assign_instructor(instructor1)

it_course1.add_students(student1, student2, student3, student4, student5)

assignment1 = CourseAssignment(1, course1, instructor1, date(2024, 4, 11))

grade = Grade(student1, course1, 95, date.today())
grade1 = Grade(student2, course1, 96, date.today())

print(it_course1.display_info())
print(assignment1.display_info())
print(grade.display_info())
print(grade1.display_info())