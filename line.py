
class Line(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return '({}, {})'.format(self.start, self.end)

    def __repr__(self):
        return 'line.Line({}, {})'.format(self.start, self.end)


