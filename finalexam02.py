class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_sum = self.x + other.x
        y_sum = self.y + other.y
        return Point(x_sum, y_sum)

    def get_distance(self, point):
        distance = (self.x-point.x)**2 + (self.y-point.y)**2
        return distance ** 0.5


p1 = Point(1, 1)
p2 = Point(2, 2)

print("거리")
print(Point.get_distance(p1, p2))

print("합")
print(Point.__add__(p1, p2).x, Point.__add__(p1, p2).y)
