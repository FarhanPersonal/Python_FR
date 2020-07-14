# Creating custom class 'Point'with constructors.
class Point:
    # Class level attribute
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")


point = Point(1, 2)

Point.default_color = "Yellow"

anotherPoint = Point(3, 4)

point.default_color = "blue"

print(point.default_color)
print(anotherPoint.default_color)

# FR: Creating attributes/properties of point object outside the class
point.z = 20

print(point.z)
