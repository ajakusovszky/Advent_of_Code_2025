from loguru import logger


def get_input_file(file_path: str) -> str:
    with open(file_path, "r") as file:
        # Read the entire content of the file into a string
        file_content = file.read()
        return file_content


def clear_lines(lines: list[str]) -> list[str]:
    new_lines = []
    for line in lines:
        stripped_line = line.strip()
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
    result = []
    found_empty = False
    for line in lines:
        if found_empty:
            result.append(line)
            continue
        if line.strip() == "":
            found_empty = True
    return result
