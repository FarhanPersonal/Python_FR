# Creating custom class 'Point'with constructors.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")


point = Point(1, 2)

# FR: Creating attributes/properties of point object outside the class
point.z = 20

print(point.z)
