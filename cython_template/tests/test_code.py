from cython_template.code import example_function


def test_example_function():
    for N in range(10):
        assert example_function(N) == 0.5 * N * (N - 1)
