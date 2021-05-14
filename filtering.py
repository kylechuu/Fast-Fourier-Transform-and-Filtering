import numpy as np
from fractions import  Fraction

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes and returns a 5X5 Gaussian filter
            Use the formula for a 2D gaussian to get the values for a 5X5 gaussian filter
        """

        # rows, cols = self.image.shape
        filter = np.zeros((5, 5), dtype = 'float')
        # sum = 0

        for row in range(-2, 3):
            for col in range(-2, 3):
                filter[row + 2][col + 2] = np.exp(-1*((row**2) + (col**2))/2) / (2 * np.pi)
                # sum += filter[row + 2][col + 2]

        return filter

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""

        filter = np.zeros((3, 3))

        filter[0][1] = filter[1][0] = filter[2][1] = filter[1][2] = -1
        filter[1][1] = 4

        return filter

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """

        rows, cols = self.image.shape
        filter_type = ["gaussian", "laplacian"]
        new_image = np.zeros((rows, cols), dtype=int)

        if filter_name not in filter_type:
            raise Exception("Sorry, no such filter")

        if filter_name == "gaussian":
            filter = self.get_gaussian_filter()

            for row in range(rows):
                for col in range(cols):
                    filter_r = filter_c = 0

                    for r in range(row - 2, row + 3):
                        for c in range(col - 2, col + 3):
                            if 0 <= r < rows and 0 <= c < cols:
                                new_image[row][col] += filter[filter_r][filter_c]*self.image[r][c]

                            filter_c += 1

                        filter_r += 1
                        filter_c = 0

        if filter_name == "laplacian":
            filter = self.get_laplacian_filter()

            for row in range(rows):
                for col in range(cols):
                    filter_r = filter_c = 0

                    for r in range(row - 1, row + 2):
                        for c in range(col - 1, col + 2):
                            if 0 <= r < rows and 0 <= c < cols:
                                new_image[row][col] += filter[filter_r][filter_c] * self.image[r][c]

                            filter_c += 1

                        filter_r += 1
                        filter_c = 0

        return new_image




