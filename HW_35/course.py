class ITCourse:
    course_count = 0

    def __init__(self, course_name, duration_weeks):
        """Initialize the ITCourse instance with a name and duration

        Parameters:
        course_name (str): The name of the course
        duration_weeks (int): The duration of the course in weeks"""

        self.course_name = course_name
        self.duration_weeks = duration_weeks
        self.enrolled_students = []
        ITCourse.course_count += 1

    def enroll_students(self, *student_names):
        """Enroll one or more students in the course.

        Parameters:
        student_name (str): The name of the student to enroll"""
        for student in student_names:
            self.enrolled_students.append(student)

        print(f"Student {student_names} have been enrolled in {self.course_name}.")

    def course_details(self):
        """Print the details of the course, including name, duration, and enrolled students"""

        print(f"Course Name: {self.course_name}")
        print(f"Duration (weeks): {self.duration_weeks}")
        print(f"{'Enrolled Students: ' if self.enrolled_students else 'No students enrolled'}"
              f"{', '.join(self.enrolled_students)}.")

    @classmethod
    def total_courses(cls):
        """Print the total number of courses created"""

        print(f"Total IT courses created: {cls.course_count}")

    @staticmethod
    def calculate_completion_date(start_date, duration_weeks):
        """Calculate the completion date of the course given a start date and duration

        Parameters:
        start_date (datetime.date): The start date of the course
        duration_weeks (int): The duration of the course in weeks"""
        from datetime import timedelta
        return start_date + timedelta(weeks=duration_weeks)


if __name__ == "__main__":
    import datetime

    qa_automation_python = ITCourse("QA Automation Python", 16)
    qa_automation_python.enroll_students('Kostiantyn Pshenyshniuk', 'Yevhenii Aizenberg', 'Daria Veresha',
                                         'Liubov Dundieva', 'Ruslan Zaslotskyi')
    qa_automation_python.course_details()
    start_date_qa = datetime.date(2024, 4, 11)
    completion_date_qa = ITCourse.calculate_completion_date(start_date_qa, qa_automation_python.duration_weeks)
    print(f"The QA Automation Python course starting on {start_date_qa} will complete on {completion_date_qa}.\n")

    python_pro = ITCourse("Python Pro", 16)
    python_pro.enroll_students('Albert Einstein', 'Marilyn Monroe', 'Elon Musk',
                               'Oprah Winfrey', 'Leonardo DiCaprio')
    python_pro.course_details()
    start_date_pro = datetime.date(2024, 5, 28)
    completion_date_pro = ITCourse.calculate_completion_date(start_date_pro, python_pro.duration_weeks)
    print(f"The Python Pro course starting on {start_date_pro} will complete on {completion_date_pro}.\n")

    ITCourse.total_courses()
