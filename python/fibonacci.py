#! /usr/bin/env python
from functools import lru_cache


def fibonacci(size: int) -> list:
    """Simple fibonacci version"""
    result = [0, 1]
    for i in range(1, size-1):
        result.append(result[i-1] + result[i])
    return result


print(fibonacci(size=12))


def recursive_fibonacci(maxLenght: int) -> list:
    """Recursive and memoized version"""

    @lru_cache(maxsize=None)
    def memo_recursive_fib(number: int):
        if number < 2:
            return number
        return memo_recursive_fib(number-1) + memo_recursive_fib(number - 2)

    return [memo_recursive_fib(i) for i in range(maxLenght)]


print(recursive_fibonacci(maxLenght=100))
