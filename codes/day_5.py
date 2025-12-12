"""
https://adventofcode.com/2025/day/5
Day 5: Cafeteria
"""

from loguru import logger

from .handle_inputs import (
    clear_lines,
    get_input_file,
    get_part_after_empty_line,
    get_part_before_empty_line,
)

file_path: str = "inputs/day_5.txt"


def _load_input() -> list[str]:
    return get_input_file(file_path).splitlines()


def p1(fn_load_input=_load_input) -> int:
    file_content = clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    logger.trace(f"{file_content=}")
    if not file_content:
        return 0
    fresh_ranges = get_part_before_empty_line(file_content)
    available = get_part_after_empty_line(file_content)
    logger.trace(f"{fresh_ranges=}")
    logger.trace(f"{available=}")
    # Convert fresh_ranges to list of tuples of integers
    fresh_ranges_int = [
        (int(fr.split("-")[0]), int(fr.split("-")[1])) for fr in fresh_ranges if fr
    ]
    spoiled = set()
    for a in available:
        found = False
        for start, end in fresh_ranges_int:
            if start <= int(a) <= end:
                found = True
                logger.trace(f"Available item {a} fits in range {start}-{end}")
                break
        if not found:
            logger.debug(f"Available item {a} does not fit in any range")
            spoiled.add(a)
    logger.debug(f"Total spoiled items: {len(spoiled)} from available {len(available)}")
    return len(available) - len(spoiled)


def p2(fn_load_input=_load_input) -> int:
    file_content = clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    logger.trace(f"{file_content=}")
    if not file_content:
        return 0
    fresh_ranges = get_part_before_empty_line(file_content)
    logger.trace(f"{fresh_ranges=}")
    # Convert fresh_ranges to list of tuples of integers
    fresh_ranges_int = [
        (int(fr.split("-")[0]), int(fr.split("-")[1])) for fr in fresh_ranges if fr
    ]
    # available_set = set()
    # for start, end in fresh_ranges_int:
    #     for item in range(start, end + 1):
    #         available_set.add(item)
    # brute force approach is slow for large ranges

    # Optimized approach to add all items in ranges to a new list, which only stores unique ranges
    fresh_ranges_int.sort()  # sort by start of range
    merged_ranges = []
    for start, end in fresh_ranges_int:
        if not merged_ranges:
            merged_ranges.append((start, end))
            logger.trace(f"Adding initial range {start}-{end}")
            continue
        last_start, last_end = merged_ranges[-1]
        if start <= last_end + 1:
            # Ranges overlap or are contiguous, merge them
            logger.trace(
                f"Merging overlapping/contiguous range {start}-{end} with {last_start}-{last_end}"
            )
            merged_ranges[-1] = (last_start, max(last_end, end))
        else:
            logger.trace(f"Adding new non-overlapping range {start}-{end}")
            merged_ranges.append((start, end))

    total_fresh = sum(end - start + 1 for start, end in merged_ranges)
    logger.debug(f"Total available items from fresh ranges: {total_fresh}")
    return total_fresh
