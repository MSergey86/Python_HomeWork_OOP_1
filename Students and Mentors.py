# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    students = []
    lectors = []

    def general_average_students(students, course):
        count = 0
        summ = 0
        for student in students:
            if course in student.courses_in_progress:
               for i in student.grades[course]:
                   summ += i
                   count += 1
        if count == 0:
            print(f"Нет студентов на курсе {course}")
        else:
            average = summ / count
            print(f'Средняя оценка за домашние задания по курсу {course}: {average}')

    def general_average_lectors(lectors, course):
        count = 0
        summ = 0
        for lector in lectors:
            if course in lector.courses_attached:
               for i in lector.grades[course]:
                   summ += i
                   count += 1
        if count == 0:
            print(f"Никто не читает лекции по курсу {course}")
        else:
            average = summ / count
            print(f'Средняя оценка за лекции по курсу {course}: {average}')


    class Student:
        def __init__(self, name, surname, gender):
            self.name = name
            self.surname = surname
            self.gender = gender
            self.finished_courses = []
            self.courses_in_progress = []
            self.grades = {}
            students.append(self)

        def rate_lect(self, lector, course, grade):
            if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
                if course in lector.grades:
                    lector.grades[course] += [grade]
                else:
                    lector.grades[course] = [grade]
            else:
                print(f'Лектор {lector.surname} не преподает {course}')
                return "Ошибка"

        def __str__(self):
            text_student = (
                 f'Имя: {self.name}\n'
                 f'Фамилия: {self.surname}\n'
                 f'Средняя оценнка за домашние задания: {self.__average_grade()}\n'
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                 f'Завершенные курсы: {", ".join(self.finished_courses)}')
            return text_student

        def __average_grade(self):
            summ = 0
            count = 0
            for grades1 in self.grades.values():
                for grade1 in grades1:
                  summ += grade1
                  count += 1
            average_grade_home_work = summ / count
            return average_grade_home_work

        def best_student(self, other):
            if float(self.__average_grade()) > float(other.__average_grade()):
                return f'{self.surname} - лучший студент'
            else:
                return f'{other.surname} - лучший студент'

    class Mentor:
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname
            self.courses_attached = []


    class Lecturer(Mentor):
        def __init__(self, name, surname):
            self.name = name
            self.surname = surname
            self.courses_attached = []
            self.grades = {}
            lectors.append(self)

        def __str__(self):
            text_lector = (
                 f'Имя: {self.name}\n'
                 f'Фамилия: {self.surname}\n'
                 f'Средняя оценнка за лекции: {self.__average_grade()}')
            return text_lector

        def __average_grade(self):
            summ = 0
            count = 0
            for grades1 in self.grades.values():
                for grade1 in grades1:
                  summ += grade1
                  count += 1
            average_grade_lect = summ / count
            return average_grade_lect

        def best_lector(self, other):
            if float(self.__average_grade()) > float(other.__average_grade()):
                return f'{self.surname} - лучший лектор'
            else:
                return f'{other.surname} - лучший лектор'

    class Reviewer(Mentor):

        def rate_hw(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                print(f'Студент {student.surname} не изучает {course}')
                return "Ошибка"

        def __str__(self):
            text_reviewer = (
                f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')
            return text_reviewer

    first_student = Student('Ruoy', 'Eman', 'your_gender')
    first_student.courses_in_progress += ['Python']
    first_student.courses_in_progress += ['Jawa']
    first_student.finished_courses += ['C++']

    second_student = Student('Сергей', 'Морозов', 'муж')
    second_student.courses_in_progress += ['Python']
    second_student.courses_in_progress += ['Jawascript']
    second_student.finished_courses += ['C#']

    cool_mentor = Reviewer('Some', 'Buddy')
    cool_mentor.courses_attached += ['Python']
    cool_mentor.courses_attached += ['Jawa']

    second_mentor = Reviewer('Игорь', 'Новиков')
    second_mentor.courses_attached += ['Python']

    cool_lector = Lecturer('Павел', 'Петров')
    cool_lector.courses_attached += ['Python']
    second_lector = Lecturer('Юрий', 'Антонов')
    second_lector.courses_attached += ['Python']

    cool_mentor.rate_hw(first_student, 'Python', 8)
    cool_mentor.rate_hw(first_student, 'Python', 7)
    cool_mentor.rate_hw(first_student, 'Python', 6)
    cool_mentor.rate_hw(first_student, 'Jawa', 5)

    cool_mentor.rate_hw(second_student, 'Python', 10)
    cool_mentor.rate_hw(second_student, 'Python', 9)
    cool_mentor.rate_hw(second_student, 'Python', 10)
    cool_mentor.rate_hw(second_student, 'Jawa', 8)

    first_student.rate_lect(cool_lector, 'Python', 5)
    first_student.rate_lect(cool_lector, 'Python', 10)
    first_student.rate_lect(second_lector, 'Python', 8)
    first_student.rate_lect(second_lector, 'Python', 9)

    print(cool_mentor)
    print(cool_lector)
    print(first_student)
    print()

    print(second_mentor)
    print(second_lector)
    print(second_student)
    print()

    print(cool_lector.best_lector(second_lector))
    print(first_student.best_student(second_student))
    print()

    general_average_students(students,"Python")
    general_average_lectors(lectors,"Python")
    general_average_lectors(lectors,"Pyth")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/