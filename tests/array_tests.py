from MonkeyScope import distribution_timer

from FortranRNG import (array_random_below,
                        array_percent_true,
                        array_random_integer,
                        array_random_range,
                        array_d,
                        array_dice,
                        array_plus_or_minus,
                        array_plus_or_minus_linear,
                        array_canonical,
                        array_random_float,
                        array_triangular,
                        array_random_index,
                        array_front_linear,
                        array_back_linear,
                        array_middle_linear,
                        array_quantum_linear)

distribution_timer(
    array_random_below, 10, 100,
    post_processor=lambda x: x[0],
    label="array_random_below",
)
distribution_timer(
    array_percent_true, 50, 100,
    post_processor=lambda x: x[0],
    label="array_percent_true",
)
distribution_timer(
    array_random_integer, 1, 10, 100,
    post_processor=lambda x: x[0],
    label="array_random_integer",
)
distribution_timer(
    array_random_range, 1, 10, 2, 100,
    post_processor=lambda x: x[0],
    label="array_random_range",
)
distribution_timer(
    array_d, 10, 100,
    post_processor=lambda x: x[0],
    label="array_d",
)
distribution_timer(
    array_dice, 10, 10, 100,
    post_processor=lambda x: x[0],
    label="array_dice",
)
distribution_timer(
    array_plus_or_minus, 3, 100,
    post_processor=lambda x: x[0],
    label="array_plus_or_minus",
)
distribution_timer(
    array_plus_or_minus_linear, 3, 100,
    post_processor=lambda x: x[0],
    label="array_plus_or_minus_linear",
)
distribution_timer(
    array_canonical, 100,
    post_processor=lambda x: int(x[0]*10),
    label="array_canonical",
)
distribution_timer(
    array_random_float, 0, 1, 100,
    post_processor=lambda x: int(x[0]*10),
    label="array_random_float",
)
distribution_timer(
    array_triangular, 0, 1, 0.3, 100,
    post_processor=lambda x: int(x[0]*10),
    label="array_triangular",
)
distribution_timer(
    array_random_index, 10, 100,
    post_processor=lambda x: x[0],
    label="array_random_index",
)
distribution_timer(
    array_front_linear, 10, 100,
    post_processor=lambda x: x[0],
    label="array_front_linear",
)
distribution_timer(
    array_back_linear, 10, 100,
    post_processor=lambda x: x[0],
    label="array_back_linear",
)
distribution_timer(
    array_middle_linear, 10, 100,
    post_processor=lambda x: x[0],
    label="array_middle_linear",
)
distribution_timer(
    array_quantum_linear, 10, 100,
    post_processor=lambda x: x[0],
    label="array_quantum_linear",
)
