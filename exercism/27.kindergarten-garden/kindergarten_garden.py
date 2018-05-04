children = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
plants = {
    "V": "Violets",
    "R": "Radishes",
    "C": "Clover",
    "G": "Grass"
}


class Garden(object):
    def __init__(self, diagram, students=children):
        self.diagram = diagram.split()
        self.students = sorted(students)

    def plants(self, student):
        idx = self.students.index(student) * 2
        student_plant = self.diagram[0][idx:idx + 2] + self.diagram[1][idx:idx + 2]
        return [plants[plant] for plant in student_plant]
