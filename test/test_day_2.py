from loguru import logger


def test_day_2_p1():
    from codes.day_2 import p1

    test_cases = [
        ([], 0),
        (["11-22"], 11 + 22),  # 11-22 has two invalid IDs, 11 and 22.
        (["95-115"], 99),  # 95-115 has one invalid ID, 99.
        (["11-22,95-115"], 11 + 22 + 99),
        (["998-1012"], 1010),  # 998-1012 has one invalid ID, 1010
        (
            ["1188511880-1188511890"],
            1188511885,
        ),  # 1188511880-1188511890 has one invalid ID, 1188511885
        (["222220-222224"], 222222),  # 222220-222224 has one invalid ID, 222222
        (["1698522-1698528"], 0),  # 1698522-1698528 contains no invalid IDs
        (
            ["38593856-38593862"],
            38593859,
        ),  # 38593856-38593862 has one invalid ID, 38593859.
        (
            ["565653-565659,824824821-824824827,2121212118-2121212124"],
            0,
        ),  # The rest of the ranges contain no invalid IDs
        (
            [
                "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
            ],
            1227775554,
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p1(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(
            f"Test case {i + 1} ({input_data}) passed: expected {expected}, got {result}"
        )


def test_day_2_p2():
    from codes.day_2 import p2

    test_cases = [
        ([], 0),
        (["11-22"], 11 + 22),  # 11-22 has two invalid IDs, 11 and 22.
        (["95-115"], 99 + 111),
        (["11-22,95-115"], 11 + 22 + 99 + 111),
        (["998-1012"], 999 + 1010),  # 998-1012 has one invalid ID, 1010
        (
            ["1188511880-1188511890"],
            1188511885,
        ),  # 1188511880-1188511890 has one invalid ID, 1188511885
        (["222220-222224"], 222222),  # 222220-222224 has one invalid ID, 222222
        (["1698522-1698528"], 0),  # 1698522-1698528 contains no invalid IDs
        (
            ["38593856-38593862"],
            38593859,
        ),  # 38593856-38593862 has one invalid ID, 38593859.
        (
            ["565653-565659,824824821-824824827,2121212118-2121212124"],
            565656 + 824824824 + 2121212121,
        ),  # The rest of the ranges contain no invalid IDs
        (
            [
                "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
            ],
            4174379265,
        ),  # example from advent of code site
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        logger.debug(f"Running test case {i + 1} with input: {input_data}")
        result = p2(lambda: input_data)
        assert result == expected, (
            f"Test case {i + 1} failed: expected {expected}, got {result}"
        )
        logger.info(
            f"Test case {i + 1} ({input_data}) passed: expected {expected}, got {result}"
        )


if __name__ == "__main__":
    test_day_2_p2()
    # To test, run:
    # uv run -m test.test_day_2
    # or using -v, -vv for more verbosity:
    # uv run runner.py test.test_day_2 -v
