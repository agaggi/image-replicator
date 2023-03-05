import datetime
import copy

import numpy as np      # PIP package
from PIL import Image   # PIP package

from canvas import Canvas

# The dimensions of what the image will be resized to
# Warning: the higher the resolution, the higher the memory usage
WIDTH, HEIGHT = (256, 256)

class GeneticAlgorithm:

    def __init__(self, image: str, population: int) -> None:

        '''Class implements methods to recreate images via a genetic algorithm through
        asexual reproduction.

        Args:
            image: The image to be replicated
            population: The number of images to produce per generation
        '''

        self.image = Image.open(image).resize((WIDTH, HEIGHT))
        self.file_type = image[image.rfind('.'):]
        self.generation = 0

        self.canvases = np.array([Canvas(self.image.size) for _ in np.arange(population)])
        self.parent = None

        # Contains the RGB values of each pixel for the original image
        self.image_RGB = np.zeros(shape=[WIDTH * HEIGHT, 3], dtype=np.uint8)
        self.canvas_RGB = np.zeros(shape=[WIDTH * HEIGHT, 3], dtype=np.uint8)


    def run(self) -> None:

        '''Runner for the GeneticAlgorithm class.'''

        self.image_RGB[:] = [self.image.getpixel((x, y)) for y in np.arange(HEIGHT)
                                                         for x in np.arange(WIDTH)]

        # Keeps running until an exact replica is made
        while not self.get_fitness():

            self.reproduce()


    def get_fitness(self) -> bool:

        '''Calculates fitness for a generation.

        Fitness is the sum of the differences in pixels between a canvas and the
        original image. Fitness is calulated for each canvas and ranked based on lowest
        value (least difference).

        Returns:
            If a replica was created or not
        '''

        best_fitness = np.Infinity

        for canvas in self.canvases:

            self.canvas_RGB[:] = [canvas.canvas.getpixel((x, y)) for y in np.arange(HEIGHT)
                                                                 for x in np.arange(WIDTH)]

            canvas_fitness = np.sum(np.abs(self.image_RGB - self.canvas_RGB))

            # The child with the best fitness becomes the parent
            if canvas_fitness < best_fitness:

                best_fitness = canvas_fitness
                self.parent = canvas

        self.log(best_fitness) if self.generation % 100 == 0 else ...
        return best_fitness == 0


    def log(self, parent_fitness: int) -> None:

        '''Outputs to the terminal the best fitness of the current generation.

        Args:
            parent_fitness: The best fitness of the generation
        '''

        # Save the best image every n generations and print its fitness
        print(f'[{datetime.datetime.now().strftime("%H:%M:%S")}]', end=' ')
        print(f"Fitness for generation {self.generation}: {parent_fitness}")

        self.parent.canvas.save(f'output/{self.generation}{self.file_type}')


    def reproduce(self) -> None:

        '''Asexual reproduction.

        The parent's triangles are taken and given the chance to mutate in an attempt
        to create better offspring.
        '''

        for canvas in self.canvases:

            canvas.triangles[:] = copy.deepcopy(self.parent.triangles)

            canvas.mutate_triangles()
            canvas.draw_triangles()

        self.generation += 1
