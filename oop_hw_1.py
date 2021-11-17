from itertools import chain


class MeanVal:

    @staticmethod
    def get_mean(dct):
        lst = list(chain(*dct.values()))
        return round(sum(lst) / len(lst), 1) if len(lst) > 0 else 0


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def estimate_lecturer(self, lecturer, course, value):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached 
                and course in self.courses_in_progress and 0 <= value <= 10):
            if course in lecturer.estimation:
                lecturer.estimation[course] += [value]
            else:
                lecturer.estimation[course] = [value]
        else:
            return 'Ошибка'

    def __str__(self):
        finished_courses_str =  str(self.finished_courses).strip('[]')
        courses_in_progress_str = str(self.courses_in_progress).strip('[]')
        str_to_return = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за д/з: {MeanVal.get_mean(self.grades)}\n'
            f'Курсы в процессе изучения: {courses_in_progress_str}\n'
            f'Завершенные курсы: {finished_courses_str}')
        return str_to_return

    def __lt__(self, some_stud):
        if isinstance(some_stud, Student):
            self_mean = MeanVal.get_mean(self.grades)
            some_stud_mean = MeanVal.get_mean(some_stud.grades)
            return self_mean < some_stud_mean
        return -1

    def __gt__(self, some_stud):
        if isinstance(some_stud, Student):
            self_mean = MeanVal.get_mean(self.grades)
            some_stud_mean = MeanVal.get_mean(some_stud.grades)
            return self_mean > some_stud_mean
        return -1

    def __le__(self, some_stud):
        if isinstance(some_stud, Student):
            self_mean = MeanVal.get_mean(self.grades)
            some_stud_mean = MeanVal.get_mean(some_stud.grades)
            return self_mean <= some_stud_mean
        return -1

    def __ge__(self, some_stud):
        if isinstance(some_stud, Student):
            self_mean = MeanVal.get_mean(self.grades)
            some_stud_mean = MeanVal.get_mean(some_stud.grades)
            return self_mean >= some_stud_mean
        return -1

    def __ne__(self, some_stud):
        if isinstance(some_stud, Student):
            self_mean = MeanVal.get_mean(self.grades)
            some_stud_mean = MeanVal.get_mean(some_stud.grades)
            return self_mean != some_stud_mean
        return -1

    def __eq__(self, some_stud):
        if isinstance(some_stud, Student):
            self_mean = MeanVal.get_mean(self.grades)
            some_stud_mean = MeanVal.get_mean(some_stud.grades)
            return self_mean == some_stud_mean
        return -1

    
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.estimation = {}
    
    def __str__(self):
        str_to_return = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {MeanVal.get_mean(self.estimation)}')
        return str_to_return

    def __lt__(self, some_lec):
        if isinstance(some_lec, Lecturer):
            self_mean = MeanVal.get_mean(self.estimation)
            some_lec_mean = MeanVal.get_mean(some_lec.estimation)
            return self_mean < some_lec_mean
        return -1

    def __gt__(self, some_lec):
        if isinstance(some_lec, Lecturer):
            self_mean = MeanVal.get_mean(self.estimation)
            some_lec_mean = MeanVal.get_mean(some_lec.estimation)
            return self_mean > some_lec_mean
        return -1

    def __le__(self, some_lec):
        if isinstance(some_lec, Lecturer):
            self_mean = MeanVal.get_mean(self.estimation)
            some_lec_mean = MeanVal.get_mean(some_lec.estimation)
            return self_mean <= some_lec_mean
        return -1

    def __ge__(self, some_lec):
        if isinstance(some_lec, Lecturer):
            self_mean = MeanVal.get_mean(self.estimation)
            some_lec_mean = MeanVal.get_mean(some_lec.estimation)
            return self_mean >= some_lec_mean
        return -1

    def __ne__(self, some_lec):
        if isinstance(some_lec, Lecturer):
            self_mean = MeanVal.get_mean(self.estimation)
            some_lec_mean = MeanVal.get_mean(some_lec.estimation)
            return self_mean != some_lec_mean
        return -1

    def __eq__(self, some_lec):
        if isinstance(some_lec, Lecturer):
            self_mean = MeanVal.get_mean(self.estimation)
            some_lec_mean = MeanVal.get_mean(some_lec.estimation)
            return self_mean == some_lec_mean
        return -1


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached 
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        str_to_return = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}')
        return str_to_return


def get_mean_for_hw(students_lst, course):
    grades_dct = {(stud.name, stud.surname): stud.grades.get(course)
                  for stud in students_lst
                  if course in stud.grades.keys()}
    return MeanVal.get_mean(grades_dct)


def get_mean_for_lections(lecturers_lst, course):
    values_dct = {(lec.name, lec.surname): lec.estimation.get(course)
                  for lec in lecturers_lst
                  if course in lec.estimation.keys()}
    return MeanVal.get_mean(values_dct)



s1 = Student('Alan', 'Wake', 'Male')
s2 = Student('Scorpion', 'Wins', 'Male')
r1 = Reviewer('Sean', 'Bean')
r2 = Reviewer('John', 'Rambo')
l1 = Lecturer('Alexander', 'The Great')
l2 = Lecturer('Ivan', 'The Terrible')
# print(s1)
# print(r1)
# print(l1)
s1.add_courses('Git')
s1.add_courses('Python Basics')
s1.add_courses('Python Advanced')
s2.add_courses('Git')
s2.add_courses('Python Basics')
s2.add_courses('Python Advanced')
r1.courses_attached = ['Git', 'Python Basics', 'Python Advanced']
r1.rate_hw(s1, 'Git', 5)
r1.rate_hw(s1, 'Python Basics', 10)
r1.rate_hw(s1, 'Python Advanced', 7)
r1.rate_hw(s1, 'Git', 8)
r1.rate_hw(s1, 'Python Basics', 9)
r1.rate_hw(s1, 'Python Advanced', 6)
r1.rate_hw(s1, 'Git', 10)
r1.rate_hw(s1, 'Python Basics', 5)
r1.rate_hw(s1, 'Python Advanced', 4)
r1.rate_hw(s2, 'Git', 4)
r1.rate_hw(s2, 'Python Basics', 5)
r1.rate_hw(s2, 'Python Advanced', 7)
r1.rate_hw(s2, 'Git', 7)
r1.rate_hw(s2, 'Python Basics', 10)
r1.rate_hw(s2, 'Python Advanced', 3)
r1.rate_hw(s2, 'Git', 8)
r1.rate_hw(s2, 'Python Basics', 6)
r1.rate_hw(s2, 'Python Advanced', 6)
# print(s1 > s2, s1 == s2, s1 != s2, sep=' : ')
# print(s1)
# print(s2)
print(s1.grades)
print(s2.grades)
print(get_mean_for_hw([s1, s2], 'Git'))
print(get_mean_for_hw([s1, s2], 'Python Basics'))