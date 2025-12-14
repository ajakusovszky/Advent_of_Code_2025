import sys

from loguru import logger


def get_input_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        # Read the entire content of the file into a string
        file_content = file.read()
        return file_content


def clear_lines(lines: list[str]) -> list[str]:
    new_lines = []
    for line in lines:
        stripped_line = line
        logger.trace(f"Processing line: '{line}' -> '{stripped_line}'")
        if stripped_line:
            if "," in stripped_line:
                new_lines.extend(
                    part.strip() for part in stripped_line.split(",") if part.strip()
                )
            elif "\n" in stripped_line:
                new_lines.extend(clear_lines(stripped_line.splitlines()))
            else:
                new_lines.append(stripped_line)
        elif new_lines:
            # but keep single empty lines in input (after Day 5 changes)
            logger.trace("Adding empty line to new_lines")
            new_lines.append("")
    return new_lines


def get_part_before_empty_line(lines: list[str]) -> list[str]:
    result = []
    for line in lines:
        if line.strip() == "":
            break
        result.append(line)
    return result


def get_part_after_empty_line(lines: list[str]) -> list[str]:
    result: list[str] = []
    found_empty = False
    for line in lines:
        if found_empty:
            result.append(line)
            continue
        if line.strip() == "":
            found_empty = True
    # first and last line should be filled
    if not result[0].strip():
        result = result[1:]
    if not result[-1].strip():
        del result[-1]
    return result


def get_transpose(lines: list[str], separator: str = " ") -> list[list[str]]:
    if not lines:
        return []
    num_columns = len([v for v in lines[0].split(separator) if v.strip() != ""])
    logger.trace(f"Number of columns detected: {num_columns}")
    columns = [[] for _ in range(num_columns)]
    for line in lines:
        if not line.strip():
            continue
        parts = [v for v in line.split(separator) if v.strip() != ""]
        for i in range(num_columns):
            columns[i].append(parts[i])
    return columns


def _find_separator_column(separator: str, start_index: int, lines: list[str]) -> int:
    # find the column index where the separator appears
    for j in range(len(lines[0])):
        if j <= start_index:
            continue
        logger.trace(f"Checking column {j}")
        found_separator_only = True
        for i, line in enumerate(lines):
            if line[j] != separator:
                found_separator_only = False
                break
        if found_separator_only:
            logger.trace(f"Separator column found at index {j}")
            return j
    logger.trace("No more separator columns found.")
    return -1


def _find_separator_indexes(separator: str, lines: list[str]) -> list[int]:
    separator_indexes = [-1]
    i = 0
    while True:
        i = _find_separator_column(separator, i, lines)
        logger.trace(f"Next separator index found at: {i}")
        if i == -1:
            break
        separator_indexes.append(i)

    logger.debug(f"Separator indexes found at: {separator_indexes}")
    return separator_indexes


def get_transpose_fixed(lines: list[str], separator: str = " ") -> list[list[str]]:
    if not lines:
        return []
    num_columns = len([v for v in lines[0].split(separator) if v.strip() != ""])
    logger.debug(f"Number of columns detected: {num_columns}")
    columns = [[] for _ in range(num_columns)]

    separator_indexes = _find_separator_indexes(separator, lines)
    if len(separator_indexes) != num_columns:
        logger.error(
            f"Number of separator columns {len(separator_indexes) - 1} does not match number of data columns {num_columns}."
        )
        sys.exit(1)
    for i, line in enumerate(lines):
        if not line.strip():  # ignore empty lines
            continue
        parts = []
        for j in range(num_columns):
            separator_index = separator_indexes[j] + 1
            if j + 1 < num_columns:
                separator_index_end = separator_indexes[j + 1]
            else:
                separator_index_end = 9999
            logger.trace(
                f"Adding value at line {i} col {j}: {line[separator_index:separator_index_end]}"
            )
            parts.append(line[separator_index:separator_index_end])
        logger.trace(f"Line {i} processed: {parts}")

        for x in range(num_columns):
            columns[x].append(parts[x])
    # # fix the operator values by stripping them
    for col in columns:
        col[len(col) - 1] = col[len(col) - 1].strip()
    logger.debug(f"Transposed columns: {columns}")
    return columns
