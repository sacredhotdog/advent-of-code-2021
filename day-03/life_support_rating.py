def rating_extraction(candidates, index, candidate_extraction):
    if len(candidates) == 1:
        return candidates[0]

    results = {0: [], 1: []}

    for candidate in candidates:
        current_bit = int(candidate[index])
        results[current_bit].append(candidate)

    next_candidates = candidate_extraction(results)

    return rating_extraction(next_candidates, index+1, candidate_extraction)


def oxygen_rating_extraction(results):
    if len(results[0]) > len(results[1]):
        return results[0]
    else:
        return results[1]


def co2_rating_extraction(results):
    if len(results[0]) > len(results[1]):
        return results[1]
    else:
        return results[0]


with open("input") as input_file:
    all_results = []

    for file_line in input_file:
        binary_number = file_line.strip()
        all_results.append(binary_number)

    oxygen_rating = rating_extraction(all_results, 0, oxygen_rating_extraction)
    co2_rating = rating_extraction(all_results, 0, co2_rating_extraction)
    converted_oxygen_rating = int(oxygen_rating, 2)
    converted_co2_rating = int(co2_rating, 2)

    print(f" -> Life support rating = oxygen_rating x co2_rating")
    print(f"                        = {oxygen_rating} x {co2_rating}")
    print(f"                        = {converted_oxygen_rating} x {converted_co2_rating}")
    print(f"                        = {converted_oxygen_rating * converted_co2_rating}")
