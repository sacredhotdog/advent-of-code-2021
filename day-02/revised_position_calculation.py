with open("input") as input_file:
    horizontal_position = 0
    depth = 0
    aim = 0

    for file_line in input_file:
        command, units_str = file_line.split()
        units = int(units_str)

        if command == "forward":
            horizontal_position += units
            depth += (aim * units)
        if command == "down":
            aim += units
        if command == "up":
            aim -= units

    print(f" -> horizontal position x depth = {horizontal_position * depth} ")
