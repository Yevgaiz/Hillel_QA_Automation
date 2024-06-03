from datetime import date, timedelta
from abc import ABC, abstractmethod


class Person(ABC):
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

    def get_full_name(self):
        return f"{self._name} {self._surname}"

    @abstractmethod
    def display_info(self):
        raise NotImplementedError("Subclasses should implement this!")


class Instructor(Person):
    def __init__(self, person_id, name, surname, years_of_experience):
        super().__init__(person_id, name, surname)
        self.years_of_experience = years_of_experience

    def display_info(self):
        return f"Name: {self._name}, Surname: {self._surname}, ID: {self._person_id}, Experience: {self.years_of_experience} years"


class Student(Person):
    def __init__(self, person_id, name, surname):
        super().__init__(person_id, name, surname)

    def display_info(self):
        return f"Name: {self._name}, Surname: {self._surname}, ID: {self._person_id}"


class Course:
    def __init__(self, course_code, title, description, duration):
        self._course_code = course_code
        self.title = title
        self.duration = duration
        self.description = description
        self._groups = []

    def get_course_code(self):
        return self._course_code

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_duration(self):
        return self.duration

    def add_group(self, it_course):
        self._groups.append(it_course)

    def get_num_groups(self):
        return f"Number of groups: {len(self._groups)}"

    def display_info(self):
        return f"Course Code: {self._course_code}, Title: {self.title}, Description: {self.description}, Duration: {self.duration} weeks"


class ITCourse:
    def __init__(self, course, assignment_date):
        self._course = course
        self._students = []
        self._instructor = None
        self.assignment_date = assignment_date
        self.end_date = assignment_date + timedelta(weeks=course.duration)
        self._course.add_group(self)

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
        instructor_info = self._instructor.get_full_name() if self._instructor else "No instructor assigned"
        students_info = [student.get_full_name() for student in self._students]
        return (
            f"ITCourse: [{self._course.display_info()} Instructor: {instructor_info}\nStudents: {', '.join(students_info)}\n"
            f"Assignment Date: {self.assignment_date}, End date: {self.end_date}]")


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


course1 = Course("QA123", "QA Automation Python", "Опануй автоматизоване тестування на Python!", 16)
it_course1 = ITCourse(course1, date(2024, 4, 11))

instructor1 = Instructor(12345, "Oleksii", "Lytvynov", 15)
student1 = Student(223421, "Kostiantyn", "Pshenyshniuk")
student2 = Student(321234, "Kateryna", "Ilnytska")
student3 = Student(321235, "Yevhenll", "Alzenberg")
student4 = Student(321236, "Taras", "Andrusiv")
student5 = Student(321237, "Darla", "Veresha")

it_course1.assign_instructor(instructor1)
it_course1.add_students(student1, student2, student3, student4, student5)

grade = Grade(student1, course1, 95, date.today())
grade1 = Grade(student2, course1, 96, date.today())

print(it_course1.display_info())
print(grade.display_info())
print(grade1.display_info())
print(course1.get_num_groups())
