import math
from Student import Student

class Rational():
    myConstVal = 2

    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        #return self.num + '/' + self.den               # Returns an error! self.num and self.den are integers. It doesn't fit in a string.
        return f"{self.num}/{self.den}"                 # Curly brackets allow you to pull integers into the string

    def __add__(self, other):
        newNum = (self.num * other.den) + (other.num * self.den)
        newDen = self.den * other.den
        gcd = math.gcd(newNum, newDen)
        return Rational(newNum//gcd, newDen//gcd)       # // allows integer division. Otherwise you'd get decimals.

    def __eq__(self, other):
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.num == other.num and self.den == other.den

oneHalf = Rational(1, 2)
print(oneHalf)
oneSixth = Rational(1, 6)
print(oneSixth)
oneHalf + oneSixth
oneHalf.__add__(oneSixth)                                # Same as the line above. Line above is shorthand for this.

bob = Student(1, "Bob", 5)

print(oneHalf == oneHalf)
print(oneHalf == bob)
print (oneHalf == Rational(1, 2))

#print(Rational.den)                                     # Error. den is not a static varible
print(Rational.myConstVal)