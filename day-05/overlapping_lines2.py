class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented

        if other is not None:
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


def main():
    with open("input") as input_file:
        lines = {}
        points_with_at_least_2_overlaps = []

        for file_line in input_file:
            start, end = file_line.strip().split(" -> ")
            x1, y1 = [int(start_coordinates) for start_coordinates in start.split(",")]
            x2, y2 = [int(end_coordinates) for end_coordinates in end.split(",")]
            vertical_line = x1 == x2
            horizontal_line = y1 == y2
            diagonal_line = abs(x1 - x2) == abs(y1 - y2)

            if vertical_line or horizontal_line or diagonal_line:
                max_x = max(x1, x2)
                max_y = max(y1, y2)
                x_step = -1 if x1 == max_x else 1
                y_step = -1 if y1 == max_y else 1
                x_range = range(x1, x2 - 1, x_step) if x_step < 0 else range(x1, x2 + 1, x_step)
                y_range = range(y1, y2 - 1, y_step) if y_step < 0 else range(y1, y2 + 1, y_step)

                if vertical_line:
                    x_range = [x1 for _ in range(0, len(y_range))]
                elif horizontal_line:
                    y_range = [y1 for _ in range(0, len(x_range))]

                for x, y in zip(x_range, y_range):
                    point = Point(x, y)
                    existing_point = lines.get(point) is not None

                    if existing_point:
                        lines[point] += 1

                        if lines[point] == 2:
                            points_with_at_least_2_overlaps.append(point)
                    else:
                        lines[point] = 1

        print(f" -> Points with at least 2 overlapping lines: {len(points_with_at_least_2_overlaps)}")


if __name__ == "__main__":
    main()
