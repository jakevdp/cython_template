"""Template for packages using Cython"""

__version__ = "1.0"

# This import will check whether the cython sources have been built,
# and if not will raise a useful error.
from . import __check_build

from .example_code import example_function
