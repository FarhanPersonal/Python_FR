# Creating custom class 'Point'with constructors.
class Point:
    # Class level attribute
    default_color = "red"

    #Class level method or factory method
    @classmethod
    def zero(cls): 
        return cls(0,0)

    #Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Instance method
    def draw(self):
        print(self.x, self.y)


point = Point.zero()

point.draw()