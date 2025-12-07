def test_day_2_p1():
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
    for input_data, expected in test_cases:
        result = p1(lambda: input_data)
        assert result == expected
