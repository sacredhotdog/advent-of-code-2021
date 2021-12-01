with open("input") as input_file:
    number_of_depth_increases = 0
    previous_depth = None

    for file_line in input_file:
        depth = int(file_line.strip())

        if previous_depth and depth > previous_depth:
            number_of_depth_increases += 1

        previous_depth = depth

    print(f" -> Number of depth increases: {number_of_depth_increases}")
