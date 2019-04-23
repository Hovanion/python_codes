import math

class Pont:
    def __init__(self, x, y):
        # szetterhívások
        self.setX(x)
        self.setY(y)

    def kulonbozoPontE(self, a):
        if(self.getX() != a.getX()):
            return True
        if(self.getY() != a.getY()):
            return True
        return False

    def tavMeres(self, a):
        return math.sqrt((self.getX() - a.getX()) ** 2 + (self.getY() - a.getY()) ** 2)

    def checkEgesz(self, num):
        if(type(num) == float):
            num = int(round(num))
            print("Kerekítettünk egyet jól!")
        if(type(num) != int):
            raise TypeError("A koordináta csak egész szám lehet, mert csak. Ezt írtad: " + str(num))
        if(abs(num) > 500):
            raise ValueError("Nincs elég hely a kenveszen (min. -500, max. 500).")

    def setX(self, x):
        self.checkEgesz(x)
        self.__x = x

    def setY(self, y):
        self.checkEgesz(y)
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y
