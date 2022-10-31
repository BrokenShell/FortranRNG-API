import MonkeyScope
import FortranRNG


def boolean_generators():
    MonkeyScope.distribution_timer(
        FortranRNG.percent_true, 33.333,
        post_processor=bool,
        label=f"FortranRNG.percent_true(33.333) => bool[True, False] : True ~= 33.333%",
    )


def integer_generators():
    MonkeyScope.distribution_timer(
        FortranRNG.random_below, 10,
        label="FortranRNG.random_below(10) => [0, 10)",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.random_integer, 1, 10,
        label="FortranRNG.random_int(1, 10) => [1, 10]",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.random_range, 2, 11, 2,
        label="FortranRNG.random_range(2, 11, 2) => [2, 10] by 2",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.d, 10,
        label="FortranRNG.d(10) => [1, 10]",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.dice, 3, 6,
        label="FortranRNG.dice(3, 6) => [3, 18] ~= 10.5",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.plus_or_minus, 3,
        label=f"FortranRNG.plus_or_minus(3) => [-3, 3]",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.plus_or_minus_linear, 3,
        label=f"FortranRNG.plus_or_minus_linear(3) => [-3, 3] ~= 0",
    )


def float_generators():
    MonkeyScope.distribution_timer(
        FortranRNG.canonical,
        post_processor=lambda x: int(x * 10),
        label="FortranRNG.canonical() => int(10x)[0, 10)",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.random_float, 1, 10,
        post_processor=int,
        label="FortranRNG.random_float(1, 10) => int[1, 10)",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.triangular, 0.0, 10.0, 5.0,
        post_processor=round,
        label=f"FortranRNG.triangular(0.0, 10.0, 5.0) => round[0, 10] ~= 5.0",
    )


def random_index_generators():
    MonkeyScope.distribution_timer(
        FortranRNG.random_index, 10,
        label=f"FortranRNG.random_index(10) => [0, 9]",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.random_index, -10,
        label=f"FortranRNG.random_index(-10) => [-10, -1]",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.front_linear, 10,
        label=f"FortranRNG.front_linear(10) => [0, 9] ~= 0",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.front_linear, -10,
        label=f"FortranRNG.front_linear(-10) => [-10, -1] ~= -10",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.back_linear, 10,
        label=f"FortranRNG.back_linear(10) => [0, 9] ~= 9",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.back_linear, -10,
        label=f"FortranRNG.back_linear(-10) => [-10, -1] ~= -1",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.middle_linear, 10,
        label=f"FortranRNG.middle_linear(10) => [0, 9] ~= 4.5",
    )
    MonkeyScope.distribution_timer(
        FortranRNG.middle_linear, -10,
        label=f"FortranRNG.middle_linear(-10) => [-10, -1] ~= -5.5",
    )


if __name__ == '__main__':
    print("\nFortranRNG Test Suite\n")
    print("Boolean Generator Tests")
    boolean_generators()
    print("Integer Generator Tests")
    integer_generators()
    print("Float Generator Tests")
    float_generators()
    print("ZeroCool Index Generator Tests")
    random_index_generators()
