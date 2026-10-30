import math
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def onXaxis(self):
        return self.y == 0

    def sameAs(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def inUnitCircle(self):
        return self.distance(point(0, 0)) <= 1

    def midpoint(self, other):
        return point((self.x + other.x) / 2, (self.y + other.y) / 2)

sixseven = point(6, 7)
sixnine = point(6, 9)
print(sixseven.midpoint(sixnine))
