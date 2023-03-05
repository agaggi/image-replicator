import numpy as np                  # PIP package
from PIL import Image, ImageDraw    # PIP package

from triangle import Triangle

NUM_TRIANGLES = 1024

class Canvas:

    def __init__(self, img_size: tuple) -> None:

        '''Class manages the image by drawing/mutating triangles.

        Args:
            size: the width and height of the original image
        '''

        self.img_size = img_size
        self.canvas = None

        # Value within np.arange defines the # of triangles per image
        self.triangles = np.array([Triangle(self.img_size) for _ in np.arange(NUM_TRIANGLES)])

        # Draws the initial canvases
        self.draw_triangles()


    def draw_triangles(self) -> None:

        '''Draws the triangles associated with a canvas.'''

        # A "blank slate"
        self.canvas = Image.new('RGB', size=(self.img_size))
        image = ImageDraw.Draw(self.canvas, 'RGBA')

        for triangle in self.triangles:

            image.polygon(triangle.get_edges(), fill=triangle.get_RGBA())


    def mutate_triangles(self) -> None:

        '''Gives triangles the chance to mutate. Color and position can be changed.'''

        for triangle in self.triangles:

            triangle.mutate_colors()
            triangle.mutate_edges()
