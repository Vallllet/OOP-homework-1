all_students = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        all_students.append(self)

    def count_avg(self):
        self.sum_grade = 0
        self.grades_count = 0
        self.avg_grade = 0
        for course, grades in self.grades.items():
            self.sum_grade += sum(grades)
            self.grades_count += len(grades)
        if self.grades_count == 0:
            self.avg_grade = 'Студент не успел получить оценки'
        else:
            self.avg_grade = self.sum_grade / self.grades_count
        return self.avg_grade

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.count_avg()} \n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}'
                f'\n')

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.courses_in_progress or self.finished_courses)\
            and course in lecturer.courses_attached:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [grade]
            else:
                lecturer.lecture_grades[course] = [grade]

        else:
            return 'It is not possible'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_grade == other.avg_grade
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade < other.avg_grade
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

    def count_avg_course(self, course):
        self.sum_grade = 0
        self.grades_count = 0
        avg_course = sum(self.grades[course])/len(self.grades[course])
        return avg_course

    @classmethod
    def count_avg_all(cls, *args, course):
        all_sum = 0
        all_count = 0
        for student in all_students:
            all_sum += student.count_avg_course(course)
            all_count += 1
        avg_all = all_sum / all_count
        return avg_all




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

all_lecturers = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}
        all_lecturers.append(self)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.count_avg()}'
                f'\n')

    def count_avg(self):
        self.average_grade = 0
        self.sum_grade = 0
        self.grades_count = 0
        for course, grades in self.lecture_grades.items():
            self.sum_grade += sum(grades)
            self.grades_count += len(grades)
        if self.grades_count == 0:
            self.average_grade = 'Лектор не успел получить оценки'
        else:
            self.average_grade = self.sum_grade / self.grades_count
        return self.average_grade

    def count_avg_course(self, course):
        self.sum_grade = 0
        self.grades_count = 0
        avg_course = sum(self.lecture_grades[course])/len(self.lecture_grades[course])
        return avg_course

    @classmethod
    def count_avg_all(cls, *args, course):
        all_sum = 0
        all_count = 0
        for lecturer in all_lecturers:
            all_sum += lecturer.count_avg_course(course)
            all_count += 1
        avg_all = all_sum / all_count
        return avg_all

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade == other.average_grade
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade < other.average_grade
        return NotImplemented

    def __le__(self, other):
        return self == other or self < other

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}'
                f'\n')


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


cool_reviewer1 = Reviewer('Some', 'Buddy')
cool_reviewer1.courses_attached += ['Python']

cool_reviewer2 = Reviewer('Once', 'Told me')
cool_reviewer2.courses_attached += ['Введение в программирование']
cool_reviewer2.courses_attached += ['Git']

best_student1 = Student('Rick', 'Astley', 'male')
best_student1.courses_in_progress += ['Python']
best_student1.add_courses('Git')
best_student1.add_courses('Введение в программирование')
cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 10)

best_student2 = Student('Guillo', 'Tine', 'female')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.add_courses('Введение в программирование')
cool_reviewer1.rate_hw(best_student2, 'Python', 7)
cool_reviewer1.rate_hw(best_student2, 'Python', 8)
cool_reviewer2.rate_hw(best_student2, 'Git', 9)

super_lecturer1 = Lecturer('Stas', 'Michailov')
super_lecturer1.courses_attached += ['Введение в программирование']
super_lecturer1.courses_attached += ['Python']
best_student1.rate_lect(super_lecturer1, 'Введение в программирование', 10)
best_student2.rate_lect(super_lecturer1, 'Python', 8)

super_lecturer2 = Lecturer('The Time', 'Itself')
super_lecturer2.courses_attached += ['Python']
super_lecturer2.courses_attached += ['Git']
best_student2.rate_lect(super_lecturer2, 'Python', 10)
best_student1.rate_lect(super_lecturer2, 'Python', 10)



print(best_student1)
print(best_student2)
print(best_student1 > best_student2)
print(best_student1 < best_student2)
print(cool_reviewer1)
print(cool_reviewer2)
print(super_lecturer1)
print(super_lecturer2)
print(Student.count_avg_all(all_students, course='Python')) #подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
print(Lecturer.count_avg_all(all_lecturers, course='Python')) #подсчет средней оценки за лекции всех лекторов в рамках курса
print(super_lecturer1 == super_lecturer2)
print(super_lecturer1 < super_lecturer2)

