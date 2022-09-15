# Python code to simulate a moving paintbrush that relies on a Markov chain
import numpy as np
import matplotlib.pyplot as plt

SMALLEST = 6.0
SMALLER = 8.0
REGULAR = 10.0
LARGER = 12.0
LARGEST = 14.0


class ArtWalker:
    def __init__(self, direction_transition_matrix, color_transition_matrix, pressure_transition_matrix):
        """
        Args:
          direction_transition_matrix (dict): transition probabilities for the Markov chain
          color_transition_matrix (dict): color probabilities for the Markov chain
          pressure_transition_matrix (dict): pressure probabilities for the Markov chain
        """
        self.direction_transition_matrix = direction_transition_matrix
        self.directions = list(direction_transition_matrix.keys())
        self.color_transition_matrix = color_transition_matrix
        self.colors = list(color_transition_matrix.keys())
        self.pressure_transition_matrix = pressure_transition_matrix
        self.pressures = list(pressure_transition_matrix.keys())

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
        """
        return np.random.choice(
            self.colors,
            p=[self.color_transition_matrix[current_color][next_color] for next_color in self.colors]
        )

    def get_next_pressure(self, current_pressure):
        """ Determine the next pressure based on the current pressure
        Args:
            current_pressure (float): the current pressure
        """
        return np.random.choice(
            self.pressures,
            p=[self.pressure_transition_matrix[float(current_pressure)][next_pressure] for
               next_pressure in self.pressures]
        )

    def walk_around(self, current_direction="N", current_color="blue", current_pressure=10,
                    path_length=100, jump_size=50):
        """Generating a path through a modified random walk with color and pressure variation.
        Args:
            current_direction (str): starting direction
            current_color (str): starting color
            current_pressure (float): starting pressure
            path_length (int): number of steps per path
            jump_size (int): size of a jump
        """
        x = np.zeros(path_length)
        y = np.zeros(path_length)
        colors = []
        pressures = []

        # for each step in discrete time, determine an x-coord, y-coord, color, and pressure
        for i in range(0, path_length):
            step_size = 1  # unless jump, the step_size is 1
            direction = self.get_next_direction(current_direction)
            current_color = self.get_next_color(current_color)
            colors.append(current_color)
            current_pressure = self.get_next_pressure(current_pressure)
            print(current_pressure)
            print(type(current_pressure))
            pressures.append(current_pressure)

            #
            # if i > 0:
            #     new_pressure_mod = self.get_next_pressure_mod(current_pressure_mod)
            #     print("mod: " + str(new_pressure_mod))
            #     new_pressure = new_pressure_mod * pressures[i-1]
            #     if new_pressure < 1:
            #         new_pressure = 1
            #     print("pressure: " + str(new_pressure))
            #     pressures[i] = new_pressure
            #     current_pressure_mod = new_pressure_mod
            #

            current_direction = direction
            if direction == "J":  # in case of jump, modify size of jump for next direction
                step_size = jump_size
                direction = self.get_next_direction(current_direction)
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
            else:  # pause, i.e. no motion, but color/pressure may change
                x[i] = x[i - 1]
                y[i] = y[i - 1]

        # for i in range(0, path_length):
        #     pressures[i] = 10
        # print(pressures)
        this_path = np.vstack((x, y, colors, pressures))
        return this_path


def main():
    walk_markov_a = ArtWalker({
        "N": {"N": 0.02, "E": 0.9, "S": 0.0, "W": 0.02, "P": 0.02, "J": 0.04},
        "E": {"N": 0.02, "E": 0.02, "S": 0.9, "W": 0.0, "P": 0.02, "J": 0.04},
        "S": {"N": 0.0, "E": 0.02, "S": 0.02, "W": 0.9, "P": 0.02, "J": 0.04},
        "W": {"N": 0.9, "E": 0.0, "S": 0.02, "W": 0.02, "P": 0.02, "J": 0.04},
        "P": {"N": 0.2, "E": 0.2, "S": 0.2, "W": 0.2, "P": 0.2, "J": 0.0},
        "J": {"N": 0.2, "E": 0.2, "S": 0.2, "W": 0.2, "P": 0.2, "J": 0.0},
    },
        {
            "blue": {"blue": 0.5, "green": 0.1, "red": 0.1, "cyan": 0.1, "magenta": 0.1, "yellow": 0.1},
            "green": {"blue": 0.1, "green": 0.5, "red": 0.1, "cyan": 0.1, "magenta": 0.1, "yellow": 0.1},
            "red": {"blue": 0.1, "green": 0.1, "red": 0.5, "cyan": 0.1, "magenta": 0.1, "yellow": 0.1},
            "cyan": {"blue": 0.1, "green": 0.1, "red": 0.1, "cyan": 0.5, "magenta": 0.1, "yellow": 0.1},
            "magenta": {"blue": 0.1, "green": 0.1, "red": 0.1, "cyan": 0.1, "magenta": 0.5, "yellow": 0.1},
            "yellow": {"blue": 0.1, "green": 0.1, "red": 0.1, "cyan": 0.1, "magenta": 0.1, "yellow": 0.5},
        },
        {
            SMALLEST: {SMALLEST: 0.0, SMALLER: 0.1, REGULAR: 0.1, LARGER: 0.1, LARGEST: 0.7},
            SMALLER: {SMALLEST: 0.1, SMALLER: 0.1, REGULAR: 0.1, LARGER: 0.6, LARGEST: 0.1},
            REGULAR: {SMALLEST: 0.0, SMALLER: 0.1, REGULAR: 0.8, LARGER: 0.1, LARGEST: 0.0},
            LARGER: {SMALLEST: 0.1, SMALLER: 0.6, REGULAR: 0.1, LARGER: 0.1, LARGEST: 0.1},
            LARGEST: {SMALLEST: 0.7, SMALLER: 0.1, REGULAR: 0.1, LARGER: 0.1, LARGEST: 0.0},
        }
    )

    start_direction = "S"  # "N" for north, "E" for east, "S" for south, "W" for west
    start_color = "cyan"  # "blue", "green", "red", "cyan", "magenta", or "yellow"
    current_pressure = REGULAR  # 0.5, 0.75, 1.0, 1.25, or 1.5
    path_length = 1000  # integer from 1 to 10,000 (above 10,000 can take a while)
    jump_size = 200  # integer 1 or greater

    path_a = walk_markov_a.walk_around(start_direction, start_color, current_pressure, path_length, jump_size)
    x_a = path_a[0][:]
    y_a = path_a[1][:]
    colors_a = path_a[2][:]
    pressures_a = path_a[3][:]

    # plotting stuff:
    plt.title("MarkovBrush (" + str(path_length) + " steps)")
    for i in range(len(path_a[0][:])):
        # plotting the corresponding x with y
        # and respective color
        plt.scatter(x_a[i], y_a[i], c=colors_a[i], marker='D', s=30, linewidth=0)
        # plt.scatter(x_a[i], y_a[i], s=pressures_a[i], c=colors_a[i], marker='.', linewidth=0)

    # PRESSURE IDEA IS VERY BAD NOT WORKING WELL VERY BAD
    # plt.plot(x_a, y_a, 'go')
    # plt.plot(x_b, y_b, 'rs')
    plt.axis('off')
    plt.gca().set_aspect('equal', adjustable='box')  # maintain 1:1 scale of the plot axes
    plt.savefig("MarkovBrush.png", bbox_inches="tight", dpi=600)
    plt.show()


if __name__ == "__main__":
    main()