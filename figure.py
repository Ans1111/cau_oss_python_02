import math

class Line:
    def __init__(self, length=1):
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
        else:
            self.__length = 1

    def set_length(self, length):
        if isinstance(length, (int, float)) and length > 0:
            self.__length = length
    
    def get_length(self):
        return self.__length

def area_square(line):
    if not isinstance(line, Line):
        return 0
    return line.get_length() ** 2

def area_circle(line):
    if not isinstance(line, Line):
        return 0
    return line.get_length() ** 2 * math.pi

def area_regular_triangle(line):
    if not isinstance(line, Line):
        return 0
    return line.get_length() ** 2 * math.sqrt(3) / 4
