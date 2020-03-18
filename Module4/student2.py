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

    def getScores(self, idx):
        return self.scores[idx-1]

    def setScore(self, idx, score):
        idx -= 1
        self.scores[idx] = score

    def getAverage(self):
        return sum(self.scores) / float(len(self.scores))

    def getHighScore(self):
        high = self.scores[0]
        for i in range(1, len(self.scores)):
            if self.scores[i] > high:
                high = self.scores[i]
        return high

#Code calls
def main():
    s = Student(1000000, "Bucky", 5)
    print(s)
    print(s.getName())
    s.setName("Cptn America")
    print(s.getName())
    print(s.setScore(1, 65))
    s.setScore(2, 76)
    s.setScore(3, 85)
    s.setScore(4, 87)
    s.setScore(5, 44)
    print(s.getScores(1))
    print(s.getAverage())
    print(s.getHighScore())

if __name__== "__main__":
    main()