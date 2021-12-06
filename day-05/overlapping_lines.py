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
        # max_x: 990, max_y: 990
        lines = {}
        points_with_at_least_2_overlaps = []

        for file_line in input_file:
            start, end = file_line.strip().split(" -> ")
            x1, y1 = [int(start_coordinates) for start_coordinates in start.split(",")]
            x2, y2 = [int(end_coordinates) for end_coordinates in end.split(",")]
            constant_x = x1 == x2
            constant_y = y1 == y2

            if constant_x or constant_y:
                if constant_x:
                    constant_coordinate = x1
                    start_coordinate = min(y1, y2)
                    end_coordinate = max(y1, y2)
                elif constant_y:
                    constant_coordinate = y1
                    start_coordinate = min(x1, x2)
                    end_coordinate = max(x1, x2)

                # Traverse the horizontal / vertical line and check for intersections
                for current_coordinate in range(start_coordinate, end_coordinate+1):
                    if constant_x:
                        point = Point(constant_coordinate, current_coordinate)
                    elif constant_y:
                        point = Point(current_coordinate, constant_coordinate)

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
