"""
https://adventofcode.com/2025/day/4
Day 4: Printing Department
"""

from loguru import logger

from .handle_inputs import get_input_file

file_path: str = "inputs/day_4.txt"


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


def _get_papercount_around(x: int, y: int, grid: list[str]) -> int:
    """counts how many papers are around the given position"""
    count = 0
    directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
            if grid[ny][nx] != ".":
                count += 1
    return count


def _set_line_with_x(line_no: int, grid: list[str], max_papers: int = 3) -> list[str]:
    """gives back a line with x where papers match the condition"""
    for i in range(len(grid[line_no])):
        if (
            grid[line_no][i] == "@"
            and _get_papercount_around(i, line_no, grid) <= max_papers
        ):
            grid[line_no] = grid[line_no][:i] + "x" + grid[line_no][i + 1 :]
    # return grid[line_no]


def p1(fn_load_input=_load_input) -> int:
    file_content = _clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    logger.trace(file_content)
    if not file_content:
        return 0

    for i in range(len(file_content)):
        logger.trace(f"Processing line {i}: {file_content[i]}")
        _set_line_with_x(i, file_content)

    logger.trace(f"End state of file content:\n{'\n'.join(file_content)}")
    total = sum(line.count("x") for line in file_content)
    logger.debug(f"Total papers to remove: {total}")
    return total


def p2(fn_load_input=_load_input) -> int:
    file_content = _clear_lines(fn_load_input())
    logger.debug(f"Loaded {len(file_content)} lines from input file.")
    logger.trace(file_content)
    if not file_content:
        return 0

    total = 0
    iteration = 0
    while True:
        iteration += 1
        logger.debug(f"Starting iteration {iteration}")
        for i in range(len(file_content)):
            logger.trace(f"Processing line {i}: {file_content[i]}")
            _set_line_with_x(i, file_content)
        total_inc = sum(line.count("x") for line in file_content)
        logger.debug(f"Iteration {iteration} removed {total_inc} papers")
        if total_inc == 0 or iteration >= 1000:
            break
        total += total_inc
        logger.trace(f"End state of file content:\n{'\n'.join(file_content)}")
        # Reset x to . for the next iteration
        for i in range(len(file_content)):
            file_content[i] = file_content[i].replace("x", ".")

    logger.debug(f"Total papers to remove: {total}")
    return total
