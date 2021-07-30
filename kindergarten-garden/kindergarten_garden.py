class Garden:
    plant = {'R': 'Radishes', 'G': 'Grass', 'C': 'Clover', 'V': 'Violets'}
    name = [ "Alice",  "Bob",   "Charlie",   "David",  "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph",  "Kincaid", "Larry" ]

    def __init__(self, diagram, students = name):
        self.diagram = [list(x) for x in diagram.split("\n")]
        self.students = sorted(students)

    def plants(self, student):
        student_plant=[]
        index = self.students.index(student) * 2 
        for i in range(2):
          student_plant += self.diagram[i][index:index+2] 
        return [Garden.plant[x] for x in student_plant]