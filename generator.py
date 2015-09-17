from __future__ import division
import math
import random

from noise import pnoise1, pnoise2, snoise2

from cell import Cell
import geometry
from island import Island
from line import Line


class IslandGenerator():
    """
    Generates an Island.
    """

    def __init__(self, radius):
        """ Initialize some pnoise generator defaults. """
        self.initial_radius = radius
        self.span = 8.0
        self.octaves = 8
        self.scale = 40

    def gen_border(self, points):
        """
        Generate a border to apply to our island to build shoreline.

        Returns a list of (x, y) points of generated pnoise.

        - Points is the number of points in the returned list.
        """
        base = random.randint(0, 5000)
        border = []
        for i in range(points + 1):
            x = float(i) * self.span / points
            y = pnoise1(x + base, self.octaves) * 1
            y += pnoise1(x + base, self.octaves + 4) * 2
            y *= self.scale
            border.append((i, y))
        return border

    def define_peak(self, polar_shore, scale=20):
        while True:
            alpha = 4.0
            theta = 1.0
            beta = 1.0 / theta
            var = random.gammavariate(alpha, beta)
            radius = var * scale
            angle = random.randint(0, 360)  # Random orientation
            for r, _ in polar_shore:
                if r < radius:  # Check that peak is within shoreline
                    break  # Repeat generation
            else:
                break  # Exit loop
        height = random.randint(20, 200)
        x, y = geometry.polar_to_rectangular((radius, angle))
        return Cell(x, y, height)

    def gen_spokes(self, rect_shore, peak):
        """
        Generate a list of lines (spokes) from start to end positions.
        """
        return [Line(point, peak) for point in rect_shore[::60]]

    def apply_noise_to_circle(self, border):
        """ Apply our noisy 'border' to our base circle. """
        radii = (self.initial_radius + y for _, y in border)  # Adjust radii
        angles = (x * math.pi / 180.0 for x, _ in border)  # Convert to radians
        return zip(radii, angles)

    def apply_peak_height(self, spoke_noise, peak):
        output_noise = []
        for i, (x, y) in enumerate(spoke_noise):
            dy = i / (len(spoke_noise) - 1) * peak.z
            y += dy
            output_noise.append((x, y))
        return output_noise

    def generate_island(self):
        isle = Island()
        isle.radius = self.initial_radius

        isle.shore_noise = self.gen_border(points=360)  # Generate random noise

        polar_shore = self.apply_noise_to_circle(isle.shore_noise)  # Wrap it around a circle
        isle.rect_shore = [Cell(geometry.polar_to_rectangular(x)) for x in polar_shore]  # Conver to (x, y)

        isle.shore_lines = []
        for index, point in enumerate(isle.rect_shore[:-1]):  # All but last one
            start = point
            end = isle.rect_shore[index + 1]  # Next point
            _line = Line(start, end)
            pixel_line = _line.discretize()
            isle.cells_to_tiles(*pixel_line)
            isle.shore_lines.append(pixel_line)

        isle.peak = self.define_peak(polar_shore)
        isle.cells_to_tiles(isle.peak)
        lines = self.gen_spokes(isle.rect_shore, isle.peak)
        isle.spokes = [x.discretize() for x in lines]
        for spoke in isle.spokes:
            spoke_noise = self.gen_border(points=len(spoke))
            spoke_noise = self.apply_peak_height(spoke_noise, isle.peak)
            spoke_cells = [Cell(pixel.x, pixel.y, z) for pixel, (_, z) in zip(spoke, spoke_noise)]
            isle.cells_to_tiles(*spoke_cells)

        isle.normalize()
        return isle

