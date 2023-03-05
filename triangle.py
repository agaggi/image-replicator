import random

MUTATION_RATE = 0.075    # % chance to mutate. Change to your likings

class Triangle:

    def __init__(self, img_size: tuple) -> None:

        '''Class defines a triangle's RGBA values and edges.
        Additional methods are included to mutate a triangle's attributes.
        '''

        self.width, self.height = img_size[0] - 1, img_size[1] - 1

        # Triangles are in RGBA format
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.a = random.randint(95, 115)

        # Coordinates for the edges of the triangle
        self.edge1 = [random.randint(0, self.width), random.randint(0, self.height)]
        self.edge2 = [random.randint(0, self.width), random.randint(0, self.height)]
        self.edge3 = [random.randint(0, self.width), random.randint(0, self.height)]


    def get_edges(self) -> tuple:

        '''Getter method that makes it easy to input the edge coordinates into the
        `ImageDraw.Draw.polygon()` method.

        Returns:
            The coordinates of each edge in a tuple
        '''

        return tuple(self.edge1), tuple(self.edge2), tuple(self.edge3)


    def get_RGBA(self) -> tuple:

        '''Getter method that makes it easy to input the RGBA values into the
        `ImageDraw.Draw.polygon()` method.

        Returns:
            The RGBA value of the triangle packed in a tuple
        '''

        return self.r, self.g, self.b, self.a


    def mutate_colors(self) -> None:

        '''Possibly mutates color and transparency by a small amount.'''

        if MUTATION_RATE > random.random():

            self.r = max(0, min(self.r + random.randint(-10, 10), 255))
            self.g = max(0, min(self.g + random.randint(-10, 10), 255))
            self.b = max(0, min(self.b + random.randint(-10, 10), 255))
            self.a = max(95, min(self.a + random.randint(-5, 5), 115))


    def mutate_edges(self) -> None:

        '''Possibly mutates edge positions by a small amount.'''

        if MUTATION_RATE > random.random():

            self.edge1[0] = max(0, min(self.width, self.edge1[0] + random.randint(-20, 20)))
            self.edge1[1] = max(0, min(self.height, self.edge1[1] + random.randint(-20, 20)))

            self.edge2[0] = max(0, min(self.width, self.edge2[0] + random.randint(-20, 20)))
            self.edge2[1] = max(0, min(self.height, self.edge2[1] + random.randint(-20, 20)))

            self.edge3[0] = max(0, min(self.width, self.edge3[0] + random.randint(-20, 20)))
            self.edge3[1] = max(0, min(self.height, self.edge3[1] + random.randint(-20, 20)))
