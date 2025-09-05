from base_implementation import *  # noqa: F403

try:  # (accelerated_implementation.py could be missing)
    from accelerated_implementation import *  # noqa: F403
except ImportError:
    pass
