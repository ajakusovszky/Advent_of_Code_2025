"""
https://adventofcode.com/2025/day/6
Day 6: Trash Compactor
"""

import sys

from loguru import logger

from .handle_inputs import (
    clear_lines,
    get_input_file,
    get_transpose,
    get_transpose_fixed,
)

file_path: str = "inputs/day_6.txt"


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def _calc_row(row: list[str]) -> int:
    result = 0
    if not row:
        return result
    operator = row[::-1][0]  # last item in the row
    items_pcs = len(row)
    logger.trace(f"Calculating row: {row[: items_pcs - 1]} with operator: {operator}")
    for i in range(items_pcs - 1):  # skip last iteration, which is the operator
        match operator:
            case "+":
                result += int(row[i])
            # case "-":
            #     result -= int(row[i])
            case "*":
                if result == 0:
                    result = 1
                result *= int(row[i])
            # case "/":
            #     if result == 0:
            #         result = int(row[i])
            #     else:
            #         result /= int(row[i])
            case _:
                logger.error(f"Unknown operator: {operator}")
                sys.exit(1)
    return result


def _calc_row_p2(row: list[str]) -> int:
    result = 0
    if not row:
        return result
    operator = row[::-1][0]  # last item in the row
    if operator not in ["*", "+"]:
        logger.error(f"Unknown operator: {operator}")
        sys.exit(1)
    num_length = len(row[0])  # width of string for numbers
    items_pcs = len(row)
    _row = row[: items_pcs - 1]  # ignore the operator column
    logger.trace(f"Calculating row: {_row} with operator: {operator}")
    for j in range(num_length):
        value = 0
        for i in range(len(_row)):
            value_str = _row[i][j]
            if value_str.strip():
                value = value * 10 + int(value_str)
            logger.trace(f"value: '{value_str}' - {value}")
        match operator:
            case "+":
                result += value
            case "*":
                if result == 0:
                    result = 1
                result *= value
    return result


def p1(fn_load_input=_load_input) -> int:
    file_content = clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    # logger.trace(f"{file_content=}")
    if not file_content:
        return 0
    problems = get_transpose(file_content)
    total = 0
    for problem in problems:
        logger.debug(f"Problem: {problem}")
        row_result = _calc_row(problem)
        logger.debug(f"Row result: {row_result}")
        total += row_result
    logger.debug(f"Total result: {total}")

    return total


def p2(fn_load_input=_load_input) -> int:
    file_content = clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    # logger.trace(f"{file_content=}")
    if not file_content:
        return 0
    problems = get_transpose_fixed(file_content)
    total = 0
    for problem in problems:
        num_length = len(problem[0])
        logger.debug(f"Problem: {problem} with length: {num_length}")
        row_result = _calc_row_p2(problem)
        logger.debug(f"Row result: {row_result}")
        total += row_result
    logger.debug(f"Total result: {total}")

    return total
