# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

 class Student:
     def __int__(self, name, surname, gender):
         self.name = name
         self.surname = surname
         self.gender = gender
         self.finished_courses = []
         self.courses_in_progress = []
         self.grades = {}

 class Mentor:
     def __init__(self, name, surname):
         self.name = name
         self.surname = surname
         self.courses_attached = []

     def rate_hw(self, student, course, grade):
         if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
             if course in student.grades:
                 student.grades[course] += [grade]
             else:
                 student.grades[course] = [grade]
         else:
             return "Ошибка"

 best_student = Student('Ruoy', 'Eman', 'your_gender')
 best_student.courses_in_progress += ['Python']

 cool_mentor = Mentor('Some', 'Buddy')
 cool_mentor.courses_attached += ['Python']

 cool_mentor.rate_hw(best_student, 'Python', 10)
 cool_mentor.rate_hw(best_student, 'Python', 10)
 cool_mentor.rate_hw(best_student, 'Python', 10)

 print(best_student.grades)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

