"""
https://adventofcode.com/2025/day/1
Day 1: Secret Entrance
"""

from handle_inputs import get_input_file
from loguru import logger


def part_one(file_path: str) -> int:
    file_content = get_input_file(file_path).splitlines()
    position = 50  # Start position of the dial
    count_of_0 = 0
    for line in file_content:
        direction, steps = line[0], int(line[1:])
        if direction == "L":
            position = (position - steps) % 100
        elif direction == "R":
            position = (position + steps) % 100
        if position == 0:
            count_of_0 += 1
    return count_of_0


def part_two(file_path: str) -> int:
    file_content = get_input_file(file_path).splitlines()
    position = 50  # Start position of the dial
    count_of_0s = 0
    i = 0

    def calculate_zeros(position: int, direction: str, steps: int) -> int:
        if direction == "L":
            position = position - steps
        elif direction == "R":
            position = position + steps

        count_of_0s = 0
        if position == 0:
            count_of_0s += 1
        else:
            count_of_0s += abs(position) // 100
        return position % 100, count_of_0s

    for line in file_content:
        i += 1
        direction, steps = line[0], int(line[1:])
        new_position, new_zeroes = calculate_zeros(position, direction, steps)
        # if steps > 500:
        #     logger.debug(
        #         f"Current position: {position}, moving {direction}{steps} - New position: {new_position}, count_of_0s: {new_zeroes}"
        #     )
        #     break
        position = new_position
        count_of_0s += new_zeroes

    return count_of_0s


if __name__ == "__main__":
    file_path = "inputs/day_1.txt"

    # logger.remove(0)
    # logger.add(sys.stderr, level="INFO")

    logger.info(f"1.1: {part_one(file_path)}")
    logger.info(f"1.2: {part_two(file_path)}")
