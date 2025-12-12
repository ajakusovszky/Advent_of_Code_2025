"""
https://adventofcode.com/2025/day/2
Day 2: Gift Shop
"""

from functools import cache

from loguru import logger

from .handle_inputs import get_input_file

file_path: str = "inputs/day_2.txt"


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def _get_parts(str_length: int) -> set[int]:
    # Since the young Elf was just doing silly patterns, you can find the invalid IDs by looking for any ID which is made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.
    logger.trace(f"Finding parts for string length: {str_length}")
    parts = set()
    if str_length % 2 == 0:
        parts.add(str_length // 2)
    return parts


@cache
def _get_parts_2(str_length: int) -> set[int]:
    logger.trace(f"Finding parts for string length: {str_length}")
    parts = set()
    if str_length <= 1:
        return parts
    # find all divisors of str_length except str_length itself
    for i in range(1, str_length):
        logger.trace(
            f"Checking divisor: {i} for length: {str_length}. Remainder: {str_length % i}"
        )
        if str_length % i == 0:
            parts.add(i)
    return parts


def _get_invalid_ids(
    id_ranges: list[str], _get_parts: callable = _get_parts
) -> list[int]:
    invalid_ids = set()

    for id_range in id_ranges:
        start_str, end_str = id_range.split("-")
        start, end = int(start_str), int(end_str)
        logger.trace(f"Processing range: {start} - {end}")
        previous_id_length = -1
        if start > end:
            logger.warning(f"Invalid range: {id_range}")
            continue

        for id in range(start, end + 1):
            if previous_id_length != len(str(id)):
                chunk_lengths = _get_parts(len(str(id)))
                logger.trace(
                    f"ID length changed: {len(str(id))}. New chunk lengths: {chunk_lengths}"
                )
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
    if not file_content:
        return 0
    id_ranges = file_content[0].split(",")
    invalid_ids = _get_invalid_ids(id_ranges)
    return sum(invalid_ids)


def p2(fn_load_input=_load_input) -> int:
    file_content = fn_load_input()
    if not file_content:
        return 0
    id_ranges = file_content[0].split(",")
    invalid_ids = _get_invalid_ids(id_ranges, _get_parts_2)
    return sum(invalid_ids)
