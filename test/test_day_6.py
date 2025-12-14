from loguru import logger

from codes.day_6 import p1, p2


def test_day_6_p1():
    test_cases = [
        ([], 0),
        (
            [
                """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
                """
            ],
            # 123 * 45 * 6 = 33210
            # 328 + 64 + 98 = 490
            # 51 * 387 * 215 = 4243455
            # 64 + 23 + 314 = 401
            33210 + 490 + 4243455 + 401,  # 4277556
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p1(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(f"Test case {i + 1} passed: expected {expected}, got {result}")


def test_day_6_p2():
    test_cases = [
        ([], 0),
        (
            [
                """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
                """
            ],
            # Reading the problems right-to-left one column at a time, the problems are now quite different:
            # The rightmost problem is 4 + 431 + 623 = 1058
            # The second problem from the right is 175 * 581 * 32 = 3253600
            # The third problem from the right is 8 + 248 + 369 = 625
            # Finally, the leftmost problem is 356 * 24 * 1 = 8544
            # Now, the grand total is 1058 + 3253600 + 625 + 8544 = 3263827.
            1058 + 3253600 + 625 + 8544,  # 3263827
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p2(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(f"Test case {i + 1} passed: expected {expected}, got {result}")


if __name__ == "__main__":
    test_day_6_p2()
    # To test, run:
    # uv run -m test.test_day_2
    # or using -v, -vv for more verbosity:
    # uv run runner.py test.test_day_2 -v
