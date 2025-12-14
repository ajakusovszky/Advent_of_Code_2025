"""
https://adventofcode.com/2025/day/7
Day 7: Laboratories
"""

from loguru import logger

from .handle_inputs import (
    clear_lines,
    get_input_file,
)

file_path: str = "inputs/day_7.txt"


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def _get_line(prev_line: str, curr_line: str) -> (str, int):
    # tranforms the curr_line while looking for beams or S at prev_line.
    # also returns the number of splits
    if curr_line is None:
        return None, 0
    if len(prev_line) != len(curr_line):
        logger.error("Lines length differ!")
        return None, 0
    line_length = len(prev_line)
    split_count = 0
    prev_line_list = list(prev_line)
    curr_line_list = list(curr_line)
    result = curr_line_list
    for i in range(line_length):
        has_split = False
        if prev_line_list[i] not in ["S", "|"]:
            continue
        if curr_line_list[i] == "^":
            # beam meets a splitter
            if 0 <= i - 1 and result[i - 1] != "^":
                has_split = True
                result[i - 1] = "|"
            if i + 1 <= line_length and result[i + 1] != "^":
                has_split = True
                result[i + 1] = "|"
            if has_split:
                split_count += 1
        else:
            #  beam (|) extends downward from S or a beam sign
            result[i] = "|"
    return "".join(result), split_count


def p1(fn_load_input=_load_input) -> int:
    file_content = clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    # logger.trace(f"{file_content=}")
    if not file_content:
        return 0
    total = 0
    prev_line = None
    for line in file_content:
        # skip empty lines
        if not line.strip():
            continue
        # at first line only
        if not prev_line:
            prev_line = line
            continue

        changed_line, split_count = _get_line(prev_line, line)
        logger.trace(f"line: {line} {changed_line} splits: {split_count}")

        line = changed_line
        prev_line = line
        total += split_count
    logger.debug(f"Total result: {total}")

    return total


def _int_to_bool_list(num: int, length: int) -> list[bool]:
    return [bool(num & (1 << n)) for n in range(length)]


def _generate_timeline(lines: list[str], seed: int) -> list[str]:
    possible_choices = len(lines) // 2
    choices = _int_to_bool_list(seed, possible_choices)
    for i in lines:
        ...


def _find_next_timeline(lines: list[str], seed: int) -> int:
    # seed is a list of 0/1 = Left/Right : list[bool]
    # at first iteration I assume that all left is a good solution
    # so this function returns the next seed value, which is changing the bottom element to go right, or the upper one if this is already at right

    # possible_choices = len(lines) // 2
    # for i in range(total_length - 1, 0, -1):
    #     line = lines[i]


def p2(fn_load_input=_load_input) -> int:
    file_content = clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    # logger.trace(f"{file_content=}")
    if not file_content:
        return 0
    total = 0

    logger.debug(f"Total result: {total}")

    return total
