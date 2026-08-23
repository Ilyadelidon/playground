"""A minimal retry decorator with exponential backoff."""

import functools
import random
import time
from typing import Callable, Tuple, Type


def retry(
    attempts: int = 3,
    base_delay: float = 0.5,
    backoff: float = 2.0,
    jitter: float = 0.1,
    exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Retry the wrapped callable on failure, backing off between attempts.

    The final attempt re-raises so callers still see the original traceback.
    """
    if attempts < 1:
        raise ValueError("attempts must be at least 1")

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = base_delay
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == attempts:
                        raise
                    time.sleep(delay + random.uniform(0, jitter))
                    delay *= backoff

        return wrapper

    return decorator
