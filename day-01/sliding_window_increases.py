class SlidingWindow:

    def __init__(self, values):
        if len(values) != 3:
            raise ValueError

        self.values = values
        self.total = 0

        for value in self.values:
            self.total += value


with open("input") as input_file:
    depths = []
    depth_count = 0

    for file_line in input_file:
        depth = int(file_line.strip())
        depths.append(depth)
        depth_count += 1

    previous_sliding_window = None
    number_of_increases = 0

    for i in range(0, depth_count):
        next_end_index = i + 3

        if next_end_index <= depth_count:
            sliding_window = SlidingWindow(depths[i:next_end_index])

            if previous_sliding_window and sliding_window.total > previous_sliding_window.total:
                number_of_increases += 1

            previous_sliding_window = sliding_window
        else:
            break

    print(f" -> Number of sliding window increases: {number_of_increases}")
