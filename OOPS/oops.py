# Class is basically a blueprint of an Object. While defining a class we should declare it by a class keyword along
# with the class Name and here the class name should start with a Capital Letter.
class Student:
    # Here def is a Keyword which is used to create a function or a method, the syntax is very simple, for example def
    # followed by the function name. The __init__ method in Python is a special method called a constructor. It is
    # automatically invoked when a new instance of a class is created. The purpose of the __init__ method is to
    # initialize the attributes of the instance with the values provided as arguments. This allows each instance of the
    # class to have its own unique set of attributes. The first parameter of the __init__ method is always self. This
    # refers to the instance being created and allows you to bind the instance's attributes to the values provided as
    # arguments.
    def __init__(self, name, email, course_name, year_of_pass, roll_no, qualification, grades):
        self.name = name
        self.email = email
        self.course_name = course_name
        self.year_of_pass = year_of_pass
        self.roll_no = roll_no
        self.qualification = qualification
        self.grades = grades

    def total_marks(self):
        marks_obtained = [
            {"Hindi": 97},
            {"Telugu": 98},
            {"English": 90},
            {"Maths": 95},
            {"Science": 90},
            {"Social": 85}
        ]
        total_sum = 0
        for subject in marks_obtained:
            for marks in subject.values():
                total_sum += marks
        return total_sum

    def calculate_grade(self):
        total_marks_obtained = self.total_marks()
        total_subjects = len(self.grades)
        average_marks = total_marks_obtained / total_subjects
        if 90 <= average_marks <= 100:
            return "A"
        elif 80 <= average_marks < 90:
            return "B"
        elif 70 <= average_marks < 80:
            return "C"
        elif 60 <= average_marks < 70:
            return "D"
        else:
            return "F"

    def info(self):
        return (f"Student Name: {self.name}\n"
                f"Email: {self.email}\n"
                f"Course Name: {self.course_name}\n"
                f"Year of Passing: {self.year_of_pass}\n"
                f"Roll No: {self.roll_no}\n"
                f"Qualification: {self.qualification}")

    def course_skill(self, skills):
        skills_list = ", ".join(skills)
        return (f"{self.name} is enrolled in the {self.course_name} course. \n"
                f"This course covers the following skills: {skills_list}.")

# Sample grades
grades = [
    {"Telugu": 89},
    {"Hindi": 90},
    {"Maths": 80},
    {"Social": 96},
    {"English": 95},
    {"Science": 100},
]

# Sample skills
skills = ["Python", "Data Analysis", "Web Development", "Machine Learning"]

# Creating an instance of the Student class
student = Student("Venkatesh", "venkateshreddy8005@gmail.com", "Python Full Stack", 2024, "20K81A0405", "ECE", grades)

# Accessing the attributes and methods
total = student.total_marks()
print(student.course_skill(skills))
print(student.info())
print("Total Marks Obtained in the Exam:",total)
print("Grade Obtaine:",student.calculate_grade())