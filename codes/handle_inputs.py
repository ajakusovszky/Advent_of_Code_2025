def get_input_file(file_path: str) -> str:
  with open(file_path, "r") as file:
    # Read the entire content of the file into a string
    file_content = file.read()
    return file_content


def get_left_list(file_path: str) -> list:
  file_content = get_input_file(file_path).splitlines()
  left_list = [int(line.split()[0]) for line in file_content]
  return left_list


def get_right_list(file_path: str) -> list:
  file_content = get_input_file(file_path).splitlines()
  right_list = [int(line.split()[1]) for line in file_content]
  return right_list


def get_array(file_path: str) -> list:
  file_content = get_input_file(file_path).splitlines()
  result = [list(map(int, line.split())) for line in file_content]
  return result


def get_array_without_spaces(file_path: str) -> list:
  file_content = get_input_file(file_path).splitlines()
  result = [list(line) for line in file_content]
  return result


def get_rules_pages(file_path: str) -> tuple[list[int], list[int]]:
  file_content = get_input_file(file_path).splitlines()
  # content is split by an empty line
  # rules are separated by "|"
  rules = [list(map(int, line.split("|"))) for line in file_content if "|" in line]
  # pages are separated by ","
  pages = [list(map(int, line.split(","))) for line in file_content if "," in line]
  return rules, pages
