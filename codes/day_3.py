"""
https://adventofcode.com/2025/day/2
Day 3: Lobby
"""

from loguru import logger

from .handle_inputs import get_input_file

file_path: str = "inputs/day_3.txt"


def _clear_lines(lines: list[str]) -> list[str]:
    new_lines = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            if "," in stripped_line:
                new_lines.extend(
                    part.strip() for part in stripped_line.split(",") if part.strip()
                )
            elif "\n" in stripped_line:
                new_lines.extend(
                    part.strip() for part in stripped_line.splitlines() if part.strip()
                )
            else:
                new_lines.append(stripped_line)
    return new_lines


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def _output_joltage(line: str, line_no: int) -> int:
    # find the highest and second highest digits in the line
    logger.trace(f"Processing line {line_no + 1}: {line}")
    digits = [int(char) for char in line if char.isdigit()]
    non_digit_chars = [char for char in line if not char.isdigit()]
    if non_digit_chars:
        logger.warning(
            f"Line {line_no + 1} contains non-digit characters: {''.join(non_digit_chars)}"
        )
    if not digits:
        return 0

    max_combo = 0
    for i, d in enumerate(digits):
        for j, d2 in enumerate(digits):
            if j <= i:
                continue
            combo = 10 * d + d2
            if combo > max_combo:
                logger.trace(
                    f"New max combo found on line {line_no + 1}: {combo} (from digits {d} and {d2} at positions {i} and {j})"
                )
                max_combo = combo
    logger.debug(f"Line {line_no + 1}: {max_combo}")
    return max_combo


# no, this takes forever
def _get_combinations(digits, length=12):
    """brute force all combinations of 12 digits"""
    if length == 0:
        return [0]
    combos = []
    for i, d in enumerate(digits):
        for sub_combo in _get_combinations(digits[i + 1 :], length - 1):
            combos.append(d * (10 ** (length - 1)) + sub_combo)
    return combos


def _get_combinations_opt(digits, length=12):
    """only consider digits higher or equal than the last chosen digit"""
    if length == 0:
        return [0]
    combos = []
    highest_digit = 0
    for i, d in enumerate(digits):
        if d <= highest_digit:
            continue
        highest_digit = d
        for sub_combo in _get_combinations_opt(digits[i + 1 :], length - 1):
            combos.append(d * (10 ** (length - 1)) + sub_combo)
    return combos


def _get_combinations_opt2(digits, length=12):
    """choose the highest digits available"""
    if length == 0 or not digits:
        return 0, None
    combos = []

    # choose all positions of the highest digit, but make sure to have enough length left to complete the combo
    def _get_positions(digits, length) -> tuple[int, list[int]]:
        if not digits or length <= 0:
            return 0, []
        highest_digit = max(digits)
        while True:
            if highest_digit == 0:
                return 0, []
            positions = [
                i
                for i, d in enumerate(digits)
                if d == highest_digit and len(digits) - i >= length
            ]
            if positions:
                break
            highest_digit -= 1
        return highest_digit, positions

    highest_digit, positions = _get_positions(digits, length)

    logger.trace(
        f"Finding combinations of length {length} with highest digit {highest_digit} at positions {positions}"
    )
    for i in positions:
        for sub_combo in _get_combinations_opt2(digits[i + 1 :], length - 1):
            if sub_combo is None:
                continue
            value = highest_digit * (10 ** (length - 1)) + sub_combo
            if value not in combos:
                combos.append(value)
                if length == 12:
                    logger.trace(
                        f"Combining highest digit {highest_digit} at position {i} with sub-combo {value}"
                    )

    return combos


def _output_joltage_12(line: str, line_no: int, length: int = 12) -> int:
    # find the highest and second highest digits in the line
    logger.trace(f"Processing line {line_no + 1}: {line}")
    digits = [int(char) for char in line if char.isdigit()]
    non_digit_chars = [char for char in line if not char.isdigit()]
    if non_digit_chars:
        logger.warning(
            f"Line {line_no + 1} contains non-digit characters: {''.join(non_digit_chars)}"
        )
    if not digits:
        return 0

    # logger.disable("")
    all_combos = _get_combinations_opt2(digits, length)
    # logger.enable("")
    all_combos.sort(reverse=True)
    max_combo = all_combos[0]
    logger.debug(
        f"Line {line_no + 1:>3}: {max_combo}, total combinations: {len(all_combos)}"
    )
    if len(all_combos) < 10:
        logger.trace(f"All combinations for line {line_no + 1}: {all_combos}")
    return max_combo


def p1(fn_load_input=_load_input) -> int:
    file_content = _clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    if not file_content:
        return 0
    total = 0
    for i, line in enumerate(file_content):
        total += _output_joltage(line, i)

    return total


def p1_with2(fn_load_input=_load_input) -> int:
    file_content = _clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    if not file_content:
        return 0
    total = 0
    for i, line in enumerate(file_content):
        total += _output_joltage_12(line, i, length=2)

    return total


def p2(fn_load_input=_load_input) -> int:
    file_content = _clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    if not file_content:
        return 0
    total = 0
    for i, line in enumerate(file_content):
        total += _output_joltage_12(line, i)

    return total
