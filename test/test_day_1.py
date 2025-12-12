def test_day_1_p1_moves():
    from codes.day_1 import p1

    test_cases = [
        ([], 0),
        (["L0"], 0),
        (["L50"], 1),
        (["L150"], 1),
        (["L50", "L0"], 1),
        (["R200"], 0),
        (
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"],
            3,
        ),  # example from advent of code site
    ]
    for input_data, expected in test_cases:
        result = p1(lambda: input_data)
        assert result == expected


def test_day_1_p2_moves():
    from codes.day_1 import p2

    test_cases = [
        (["L0"], 0),
        (["L50"], 1),
        (["L150"], 2),
        (["L50", "L0"], 1),
        (["R200"], 2),
        (["L250", "R150"], 4),  # 50-250=-200 →3, 0+150=150 →1, total 4
        (["R350"], 4),  # 50+350=400 → 4
        (["R450"], 5),  # 50+450=500 → 5
        (["L450"], 5),  # 50-450=-400 → 5
        (
            ["R99", "L199", "R300"],
            6,
        ),  # 50+99=149 →1, 49-199=-150 →2, 50+300=350 →3, total 6
        (
            ["L99", "R199", "L300"],
            6,
        ),  # 50-99=-49 →1, 51+199=250 →2, 50-300=-250 →3, total 6
        (
            ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"],
            6,
        ),  # example from advent of code site
    ]
    for input_data, expected in test_cases:
        result = p2(lambda: input_data)
        assert result == expected


if __name__ == "__main__":
    test_day_1_p2_moves()
    # To test, run:
    # uv run -m test.test_day_1
