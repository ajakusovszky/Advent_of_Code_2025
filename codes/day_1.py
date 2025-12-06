"""
https://adventofcode.com/2025/day/1
Day 1: Secret Entrance
"""

from loguru import logger

from .handle_inputs import get_input_file

file_path: str = "inputs/day_1.txt"


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def p1(fn_load_input=_load_input) -> int:
    file_content = fn_load_input()
    position = 50  # Start position of the dial
    count_of_0 = 0
    for line in file_content:
        direction, steps = line[0], int(line[1:])
        if steps == 0:
            logger.warning("Steps is 0, no movement.")
            continue
        if direction == "L":
            position = (position - steps) % 100
        elif direction == "R":
            position = (position + steps) % 100
        if position == 0:
            count_of_0 += 1
    return count_of_0


def _calculate_zeros(position: int, direction: str, steps: int) -> int:
    # count the number of times any click causes the dial to point at 0, regardless of whether it happens during a rotation or at the end of one.
    logger.trace(f"_ Calculating zeros: initial_position={position} {direction}{steps}")
    if direction not in ("L", "R"):
        raise logger.error(f"Invalid direction: {direction}")
    if steps == 0:
        logger.warning("Steps is 0, no movement.")
        return position, 0

    if direction == "L":
        new_position = position - steps
    elif direction == "R":
        new_position = position + steps

    count_of_0s = abs(new_position) // 100
    if direction == "L" and position > 0 and new_position <= 0:
        # crossing zero when moving left
        count_of_0s += 1
    logger.trace(
        f"{new_position=} {abs(new_position) // 100=} {new_position%100=} {count_of_0s=}"
    )
    return new_position % 100, count_of_0s


def p2(fn_load_input=_load_input) -> int:
    file_content = fn_load_input()
    position = 50  # Start position of the dial
    count_of_0s = 0
    highest_L = ""
    highest_R = ""

    for i, line in enumerate(file_content):
        direction, steps = line[0], int(line[1:])
        # just for debugging purposes log the highest L and R moves
        if direction == "L":
            if steps > int(highest_L[1:] or "0"):
                highest_L = line
        else:
            if steps > int(highest_R[1:] or "0"):
                highest_R = line
        new_position, new_zeroes = _calculate_zeros(position, direction, steps)
        position = new_position
        count_of_0s += new_zeroes

    logger.debug(f"Highest L move: {highest_L}, Highest R move: {highest_R}")
    return count_of_0s


def p2_test():
    # run tests for p2 function, use -vv for more verbose output
    test_cases = [
        (["L0"], 0),
        (["L50"], 1),
        (["L150"], 2),
        (["L50", "L0"], 1),
        (["R200"], 2),
        (["L250", "R150"], 4),  # 50-250=-200 →3, 0+150=150 →1, total 4
        (["R350"], 4),  # 50+350=400 → 4
        (["R450"], 5),  # 50+450=500 → 5
        (["L450"], 5),  # 50-450=-400 → 5
        (
            ["R99", "L199", "R300"],
            6,
        ),  # 50+99=149 →1, 49-199=-150 →2, 50+300=350 →3, total 6
        (
            ["L99", "R199", "L300"],
            6,
        ),  # 50-99=-49 →1, 51+199=250 →2, 50-300=-250 →3, total 6
        (
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"],
            6,
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = p2(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(
            f"Test case {i + 1} ({input_data}) passed: expected {expected}, got {result}"
        )


if __name__ == "__main__":
    # logger.remove(0)
    # logger.add(sys.stderr, level="INFO")

    logger.info(f"1.1: {p1()}")
    logger.info(f"1.2: {p2()}")
