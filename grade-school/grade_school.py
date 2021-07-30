class School:
    def __init__(self):
        self.student_grade = {}

    def add_student(self, name, grade):
        self.student_grade[name] = grade

    def roster(self):
        new_list = []
        student = list(self.student_grade.items())
        sort_student = sorted(student, key = lambda x:(x[1],x[0]))
        
        for i in range(len(sort_student)):
                new_list.append(sort_student[i][0])
        return new_list

    def grade(self, grade_number):
        return [i for i in sorted(self.student_grade.keys()) if self.student_grade[i] == grade_number]
