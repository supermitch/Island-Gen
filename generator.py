
class IslandGenerator():
    """ Generates a random graph of noise. (Not really an Island) """
    def __init__(self):
        """ Initialize some pnoise generator defaults. """
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
        x, y = polar_to_rectangular((radius, angle))
        return cell.Cell(x, y, height)

    def gen_spokes(self, rect_shore, peak):
        """
        Generate a list of lines (spokes) from start to end positions.
        """
        return [line.Line(point, peak) for point in rect_shore[::60]]

