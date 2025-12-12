from loguru import logger

from codes.day_3 import p1, p1_with2, p2


def test_day_3_p1():
    test_cases = [
        ([], 0),
        (["987654321111111"], 98),
        (
            [
                """
                987654321111111
                811111111111119
                234234234234278
                818181911112111
                """
            ],
            98 + 89 + 78 + 92,
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p1(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(f"Test case {i + 1} passed: expected {expected}, got {result}")


def test_day_3_p2():
    test_cases = [
        ([], 0),
        (
            [
                "5336553644444345344544134246423443634474453456455433543434354444344554344336446734443434424442135474"
            ],
            77,
        )(["987654321111111"], 987654321111),
        (["811111111111119"], 811111111119),
        (["234234234234278"], 434234234278),
        (["818181911112111"], 888911112111),
        (
            [
                """
                987654321111111
                811111111111119
                234234234234278
                818181911112111
                """
            ],
            987654321111 + 811111111119 + 434234234278 + 888911112111,
        ),  # example from advent of code site
        (
            [
                "2323969243372322938332526337221165933235227131687296213252662531524437527284729253511334229133235436"
            ],
            999999935436,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p2(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(f"Test case {i + 1} passed: expected {expected}, got {result}")


def test_day_3_p1_with2():
    test_cases = [
        ([], 0),
        (
            [
                "5336553644444345344544134246423443634474453456455433543434354444344554344336446734443434424442135474"
            ],
            77,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p1_with2(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(f"Test case {i + 1} passed: expected {expected}, got {result}")


if __name__ == "__main__":
    test_day_3_p2()
    # To test, run:
    # uv run -m test.test_day_2
    # or using -v, -vv for more verbosity:
    # uv run runner.py test.test_day_2 -v
