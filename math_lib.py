import math
class TriangleCalculator:
    __instance = None


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        pass


    def Right_Triangle(a, b):
        return 0.5*a*b
    

    def Equilateral_Triangle(a):
        return (a**2 * math.sqrt(3))/4

    
    def Isoceles_Triangle(a, b):
        return 0.5 * b * math.sqrt(((a+0.5*b)-(a+0.5*b)))
