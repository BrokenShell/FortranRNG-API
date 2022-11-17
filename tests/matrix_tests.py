from MonkeyScope import distribution_timer

from FortranRNG import (matrix_random_below,
                        matrix_percent_true,
                        matrix_random_integer,
                        matrix_random_range,
                        matrix_d,
                        matrix_dice,
                        matrix_plus_or_minus,
                        matrix_plus_or_minus_linear,
                        matrix_canonical,
                        matrix_random_float,
                        matrix_triangular,
                        matrix_random_index,
                        matrix_front_linear,
                        matrix_back_linear,
                        matrix_middle_linear,
                        matrix_quantum_linear)

size = (10, 10)

distribution_timer(
    matrix_random_below, 10, *size,
    post_processor=lambda x: x[0][0],
    label=f"matrix_random_below",
)
distribution_timer(
    matrix_percent_true, 50, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_percent_true",
)
distribution_timer(
    matrix_random_integer, 1, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_random_integer",
)
distribution_timer(
    matrix_random_range, 1, 10, 2, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_random_range",
)
distribution_timer(
    matrix_d, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_d",
)
distribution_timer(
    matrix_dice, 10, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_dice",
)
distribution_timer(
    matrix_plus_or_minus, 3, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_plus_or_minus",
)
distribution_timer(
    matrix_plus_or_minus_linear, 3, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_plus_or_minus_linear",
)
distribution_timer(
    matrix_canonical, *size,
    post_processor=lambda x: int(x[0][0]*10),
    label="matrix_canonical",
)
distribution_timer(
    matrix_random_float, 0, 1, *size,
    post_processor=lambda x: int(x[0][0]*10),
    label="matrix_random_float",
)
distribution_timer(
    matrix_triangular, 0, 1, 0.3, *size,
    post_processor=lambda x: int(x[0][0]*10),
    label="matrix_triangular",
)
distribution_timer(
    matrix_random_index, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_random_index",
)
distribution_timer(
    matrix_front_linear, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_front_linear",
)
distribution_timer(
    matrix_back_linear, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_back_linear",
)
distribution_timer(
    matrix_middle_linear, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_middle_linear",
)
distribution_timer(
    matrix_quantum_linear, 10, *size,
    post_processor=lambda x: x[0][0],
    label="matrix_quantum_linear",
)
