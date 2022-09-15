"""
Bjorn Ludwig
CSCI 3725
M3: A Markov Distinction
09/15/22
The following Python code simulates a "paintbrush" that relies on a Markov chain to move, based on a random
walk. One transition matrix determines the direction (north, east, south, west, pause, jump) based on the current
direction, and the other transition matrix determines the color (blue, green, red, cyan, magenta, yellow) based
off of the current color. The user may adjust any of the five variables starting in line 131, per the
respective constraints. The user may also adjust the transition matrices starting in line 105, where the
commented out matrix is an example of a variation.
"""

import numpy as np
import matplotlib.pyplot as plt

POINT = "."
PIXEL = ","
CIRCLE = "o"
SQUARE = "s"
DIAMOND = "D"


class ArtWalker:
    def __init__(self, direction_transition_matrix, color_transition_matrix):
        """
        Args:
          direction_transition_matrix (dict): transition probabilities for the Markov chain
          color_transition_matrix (dict): color probabilities for the Markov chain
        """
        self.direction_transition_matrix = direction_transition_matrix
        self.directions = list(direction_transition_matrix.keys())
        self.color_transition_matrix = color_transition_matrix
        self.colors = list(color_transition_matrix.keys())

    def get_next_direction(self, current_direction):
        """ Determine the direction to move based on the current direction
        Args:
            current_direction (str): the current direction of motion
        """
        return np.random.choice(
            self.directions,
            p=[self.direction_transition_matrix[current_direction][next_direction] for next_direction in
               self.directions]
        )

    def get_next_color(self, current_color):
        """ Determine the next color based on the current color
        Args:
            current_color (str): the current color
        Returns:
            (str): next color
        """
        return np.random.choice(
            self.colors,
            p=[self.color_transition_matrix[current_color][next_color] for next_color in self.colors]
        )

    def walk_around(self, current_direction="N", current_color="blue", path_length=100, jump_size=50):
        """Generating a path through a modified random walk with color variation.
        Args:
            current_direction (str): starting direction
            current_color (str): starting color
            path_length (int): number of steps per path
            jump_size (int): size of a jump
        Returns:
            path (array): stores coordinate and color info
        """
        x = np.zeros(path_length)
        y = np.zeros(path_length)
        colors = []

        # for each step in discrete time, determine an x-coord, y-coord, and color
        for i in range(0, path_length):
            step_size = 1  # unless jump, the step_size is 1
            direction = self.get_next_direction(current_direction)
            current_color = self.get_next_color(current_color)
            colors.append(current_color)
            current_direction = direction

            if direction == "J":  # in case of jump, modify size of jump for next direction
                step_size = jump_size
                direction = self.get_next_direction(current_direction)
                current_direction = direction
            if direction == "N":  # move north
                x[i] = x[i - 1]
                y[i] = y[i - 1] + step_size
            elif direction == "E":  # move east
                x[i] = x[i - 1] + step_size
                y[i] = y[i - 1]
            elif direction == "S":  # move south
                x[i] = x[i - 1]
                y[i] = y[i - 1] - step_size
            elif direction == "W":  # move west
                x[i] = x[i - 1] - step_size
                y[i] = y[i - 1]
            else:  # pause, i.e. no motion, but color/texture may change
                x[i] = x[i - 1]
                y[i] = y[i - 1]

        this_path = np.vstack((x, y, colors))
        return this_path


def main():
    walk_markov_a = ArtWalker(
        {
            "N": {"N": 0.5, "E": 0.1, "S": 0.1, "W": 0.1, "P": 0.1, "J": 0.1},  # may adjust, but values of each
            "E": {"N": 0.1, "E": 0.5, "S": 0.1, "W": 0.1, "P": 0.1, "J": 0.1},  # row MUST sum to 1.0
            "S": {"N": 0.1, "E": 0.1, "S": 0.5, "W": 0.1, "P": 0.1, "J": 0.1},
            "W": {"N": 0.1, "E": 0.1, "S": 0.1, "W": 0.5, "P": 0.1, "J": 0.1},
            "P": {"N": 0.2, "E": 0.2, "S": 0.2, "W": 0.2, "P": 0.0, "J": 0.2},
            "J": {"N": 0.2, "E": 0.2, "S": 0.2, "W": 0.2, "P": 0.2, "J": 0.0},
        },
        # {
        #     "N": {"N": 0.02, "E": 0.9, "S": 0.0, "W": 0.02, "P": 0.02, "J": 0.04},  # optional direction
        #     "E": {"N": 0.02, "E": 0.02, "S": 0.9, "W": 0.0, "P": 0.02, "J": 0.04},  # matrix variation
        #     "S": {"N": 0.0, "E": 0.02, "S": 0.02, "W": 0.9, "P": 0.02, "J": 0.04},
        #     "W": {"N": 0.9, "E": 0.0, "S": 0.02, "W": 0.02, "P": 0.02, "J": 0.04},
        #     "P": {"N": 0.2, "E": 0.2, "S": 0.2, "W": 0.2, "P": 0.0, "J": 0.2},
        #     "J": {"N": 0.2, "E": 0.2, "S": 0.2, "W": 0.2, "P": 0.2, "J": 0.0},
        # },
        {
            "blue": {"blue": 0.5, "green": 0.15, "red": 0.05, "cyan": 0.2, "magenta": 0.05, "yellow": 0.05},
            "green": {"blue": 0.2, "green": 0.5, "red": 0.05, "cyan": 0.05, "magenta": 0.15, "yellow": 0.05},
            "red": {"blue": 0.05, "green": 0.15, "red": 0.5, "cyan": 0.05, "magenta": 0.2, "yellow": 0.05},
            "cyan": {"blue": 0.2, "green": 0.15, "red": 0.05, "cyan": 0.5, "magenta": 0.05, "yellow": 0.05},
            "magenta": {"blue": 0.05, "green": 0.05, "red": 0.2, "cyan": 0.15, "magenta": 0.5, "yellow": 0.05},
            "yellow": {"blue": 0.05, "green": 0.2, "red": 0.15, "cyan": 0.05, "magenta": 0.05, "yellow": 0.5},
        }
    )

    # user may adjust the following 5 variables:
    start_direction = "S"  # "N" for north, "E" for east, "S" for south, "W" for west
    start_color = "cyan"  # "blue", "green", "red", "cyan", "magenta", or "yellow"
    texture = CIRCLE  # POINT, PIXEL, CIRCLE, SQUARE, or DIAMOND
    path_length = 1000  # integer from 1 to 10,000 (above 10,000 can take a while)
    jump_size = 1  # integer 1 or greater

    path_a = walk_markov_a.walk_around(start_direction, start_color, path_length, jump_size)
    x_a = path_a[0][:]
    y_a = path_a[1][:]
    colors_a = path_a[2][:]

    plt.title("MarkovBrush (" + str(path_length) + " steps, jump size of " + str(jump_size) + ")")
    for i in range(len(path_a[0][:])):  # plotting the corresponding x and y with respective color and texture
        plt.scatter(x_a[i], y_a[i], s=10, c=colors_a[i], marker=texture, linewidth=0)

    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')  # maintain 1:1 scale of the plot axes
    plt.savefig("MarkovBrush.png", bbox_inches="tight", dpi=600)
    plt.show()


if __name__ == "__main__":
    main()
