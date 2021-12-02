with open("input") as input_file:
    horizontal_position = 0
    depth = 0

    for file_line in input_file:
        command, units_str = file_line.split()
        units = int(units_str)

        if command == "forward":
            horizontal_position += units
        if command == "down":
            depth += units
        if command == "up":
            depth -= units

    print(f" -> horizontal position x depth = {horizontal_position * depth} ")
