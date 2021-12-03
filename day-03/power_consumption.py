results = {}
bit_count = 12

for index in range(0, bit_count):
    results[index] = {0: 0, 1: 0}

with open("input") as input_file:
    for file_line in input_file:
        binary_number = file_line.strip()

        for index in range(0, bit_count):
            bit = int(binary_number[index])
            results[index][bit] += 1

    gamma_rate = ""
    epsilon_rate = ""

    for index in range(0, bit_count):
        gamma_bit = 0 if results[index][0] > results[index][1] else 1
        gamma_rate = f"{gamma_rate}{gamma_bit}"

        epsilon_bit = 0 if gamma_bit == 1 else 1
        epsilon_rate = f"{epsilon_rate}{epsilon_bit}"

    converted_gamma_rate = int(gamma_rate, 2)
    converted_epsilon_rate = int(epsilon_rate, 2)
    power_consumption = converted_gamma_rate * converted_epsilon_rate

    print(f" -> Power consumption = gamma_rate x epsilon_rate")
    print(f"                      = {gamma_rate} x {epsilon_rate}")
    print(f"                      = {converted_gamma_rate} x {converted_epsilon_rate}")
    print(f"                      = {converted_gamma_rate * converted_epsilon_rate}")
