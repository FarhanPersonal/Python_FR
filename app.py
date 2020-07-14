# Creating custom class 'Point'
class Point:
    def draw(self):
        print("draw")


# Creating object of Point class
point = Point()

point.draw()

# Checking of type of 'point' object which is 'Point'
print(type(point))

# Checking if 'point' is an instance of class 'Point', which is true.
print(isinstance(point, Point))
