import collections


def gen_spokes():
    data = [
        ((650, 450), (458, 439)),
        ((550, 624), (458, 439)),
        ((351, 621), (458, 439)),
        ((250, 450), (458, 439)),
        ((338, 257), (458, 439)),
        ((549, 276), (458, 439))
    ]
    Spoke = collections.namedtuple('Spoke', 'start, end')
    return [(Spoke(points[0], points[1])) for points in data]


def spokes_to_pixels(spokes):
    for spoke in spokes[:1]:
        print(spoke)
        left = min(spoke.start[0], spoke.end[0])
        right = max(spoke.start[0], spoke.end[0])
        top  = min(spoke.start[1], spoke.end[1])
        bottom = max(spoke.start[1], spoke.end[1])
        print('Span: ({}, {}) ({}, {})'.format(left, right, top, bottom))
        for x in range(left, right + 1):
            for y in range(top, bottom + 1):
                pass

def main():
    spokes = gen_spokes()
    spokes_to_pixels(spokes)


if __name__ == '__main__':
    main()

