#! /usr/bin/env python3

import sys
import os
import glob

from genetic import GeneticAlgorithm

def input_check(image: str, population: int) -> bool:

    '''Checks the validity of the arguments entered by the user.

    Args:
        image: The path to the source image
        population: Population size

    Returns:
        If any errors occurred
    '''

    errors = False

    if not os.path.exists(image):

        print(f'File "{image}" does not exist.')
        errors = True

    if population < 1:

        print('Asexual reproduction requires a population of 1 or more.')
        errors = True

    return errors


def main() -> None:

    '''Initializes and runs the program.'''

    try:

        # Passed-in arguments
        image_path = sys.argv[1]
        population = int(sys.argv[2])

    except IndexError:

        exit('Program should be run with 2 arguments: image path and population')

    errors = input_check(image_path, population)

    if not errors:

        # Create the output folder if it does not exist
        if not os.path.exists('output'):

            os.makedirs('output')

        # Clear output from previous run
        output_folder = glob.glob('output/*')

        for image in output_folder:

            os.remove(image)

        algorithm = GeneticAlgorithm(image_path, population)
        algorithm.run()


if __name__ == '__main__':

    main()
