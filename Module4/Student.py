class Student():
    def __init__(self, studentId, name, number):
        self.studentId = studentId
        self.name = name
        self.scores = [0] * number

    def __str__(self):
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

    def getStudentId(self):
        return self.studentId

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getScore(self, whichTest):
        return self.scores[whichTest - 1]

    def setScore(self, whichTest, score):
        self.scores[whichTest - 1] = score
        return self.getScore(whichTest)






s = Student(10000, "Bucky", 7)

print(s.setScore(1, 100))