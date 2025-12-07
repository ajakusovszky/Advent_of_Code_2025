"""
https://adventofcode.com/2025/day/1
Day 1: Secret Entrance
"""

from loguru import logger

from .handle_inputs import get_input_file

file_path: str = "inputs/day_2.txt"


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def _get_parts(str_length: int) -> set[int]:
    parts = set()
    for i in range(2, str_length):
        if str_length % i == 0:
            parts.add(i)
    return parts


def _get_invalid_ids(id_ranges: list[str]) -> list[int]:
    seen = set()
    invalid_ids = set()

    for id_range in id_ranges:
        start_str, end_str = id_range.split("-")
        start, end = int(start_str), int(end_str)
        previous_id_length = -1
        if start > end:
            logger.warning(f"Invalid range: {id_range}")
            continue

        for id in range(start, end):
            if previous_id_length != len(str(id)):
                chunk_lengths = _get_parts(len(str(id)))
                previous_id_length = len(str(id))
                logger.debug(f"Checking ID: {id} with parts: {chunk_lengths}")

            for part in chunk_lengths:
                # add to a set to avoid duplicate work
                chunks = (str(id)[i : i + part] for i in range(0, len(str(id)), part))
                logger.trace(f"ID: {id} split into chunks of size {part}: {chunks}")
                if len(set(chunks)) == 1:
                    invalid_ids.add(id)
                    logger.debug(f"Invalid ID found: {id} with part size {part}")

    return list(invalid_ids)


def p1(fn_load_input=_load_input) -> int:
    file_content = fn_load_input()
    id_ranges = file_content[0].split(",")
    invalid_ids = _get_invalid_ids(id_ranges)
    return sum(invalid_ids) if len(invalid_ids) > 0 else 0


def p1_test():
    from codes.day_2 import p1

    test_cases = [
        ([], 0),
        (
            [
                "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
            ],
            1227775554,
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        result = p1(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(
            f"Test case {i + 1} ({input_data}) passed: expected {expected}, got {result}"
        )
