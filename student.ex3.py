class Student:


    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.means = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def rate_lecturer(self, lecturer, course, grade):
            if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'

    def __str__(self):
        try:
            for key,values in self.grades.items():
                means = sum(values)/len(values)
                self.means = means
            return f'Имя {self.name}\n'\
            f'Фамилия {self.surname}\n'\
            f'Средняя оценка за домашнее задание: {means}\n'\
            f'Курсы в процессе обучения: {self.courses_in_progress}\n'\
            f'Завершенные курсы: {self.finished_courses}'
        except ZeroDivisionError:
             print('Недостаточно данных')
        #self.means = means

        def __gt__(self, other):
            if not isinstance(other, Lecterer):
                print('Такого студента не существует.')
            return self.means > other.means

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def __str__(self):
        return f'Имя {self.name}\n' \
               f'Фамилия {self.surname}\n'
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.means = 0
    def __str__(self,name):
        print(f'Имя{name}')
        print(f'Фамилия {surname}')
        print(self.grades.mean())
    def __str__(self):
        try:
            for key, values in self.grades.items():
                means = sum(values) / len(values)
                self.means = means
            return f'Имя {self.name}\n'\
                 f'Фамилия {self.surname}\n'\
                 f'Средняя оценка за лекцию: {means}\n'
        except ZeroDivisionError:
             print('Недостаточно данных')
        #self.means = means
    def __gt__(self,other):
        if not isinstance(other,Lecterer):
            print('Такого лектора не существует.')
        return self.means > other.means

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self,name):
        print(f'Имя{name}')
        print(f'Фамилия {surname}')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses = ['Java','C+']
cool_reviewer = Reviewer('Some', 'Buddy',)
cool_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_lecturer = Lecturer('Ivanov','Ivan')
best_lecturer.courses_attached += ['Python']
grades_from_stud = Student('Ruoy', 'Eman', 'your_gender')
grades_from_stud.finished_courses += ['Python']
grades_from_stud.rate_lecturer(best_lecturer, 'Python', 10)
grades_from_stud.rate_lecturer(best_lecturer, 'Python', 9)
grades_from_stud.rate_lecturer(best_lecturer, 'Python', 10)


worse_student = Student('Dont', 'Know', 'your_gender')
worse_student.courses_in_progress += ['Java']

cool_reviewer = Reviewer('Some', 'Buddy',)
cool_reviewer.courses_attached += ['Java']

cool_reviewer.rate_hw(worse_student, 'Java', 1)
cool_reviewer.rate_hw(worse_student, 'Java', 2)
cool_reviewer.rate_hw(worse_student, 'Java', 3)

evil_lecturer = Lecturer('Dont','Understand')
evil_lecturer.courses_attached += ['Java']
grades_from_stud = Student('Dont', 'Know', 'your_gender')
grades_from_stud.finished_courses += ['Java']
grades_from_stud.rate_lecturer(evil_lecturer, 'Java', 3)
grades_from_stud.rate_lecturer(evil_lecturer, 'Java', 4)
grades_from_stud.rate_lecturer(evil_lecturer, 'Java', 3)




print(best_student.grades)
print(best_lecturer.grades)
print(best_student)
print(best_lecturer)

print(worse_student.grades)
print(evil_lecturer.grades)
print(worse_student)
print(evil_lecturer)
print(best_student.means > worse_student.means)
print(best_lecturer.means > evil_lecturer.means)