import math

class AreaCalc:
    # TODO: Implement calculate method
    pass
    def calculate(self, length: int, width=None):
        if width:
            return length * width
        else:
            return round(length * length * math.pi, 2)

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
