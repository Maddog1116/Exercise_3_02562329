class Circle:
    def __init__(self, centre, radius):
        self.centre = tuple(centre)
        self.radius = radius

    def __contains__(self, point):
        dx = point[0] - self.centre[0]
        dy = point[1] - self.centre[1]
        distance = (dx**2 + dy**2)**0.5
        return distance <= self.radius