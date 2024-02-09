class Point:
    def __init__(self, x=0, y=0):
        self.move(x, y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def dist(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
