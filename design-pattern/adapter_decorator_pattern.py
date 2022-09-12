"""
    Adapter pattern : 재사용하려는 클래스가 제공하는 인터페이스와 클라이언트가 사용하는 인터페이스가 다를 때 연결
"""

"""
    Decorator pattern : 함수에 확장된 기능을 부여
    # data validation
    # caching
    # logging
    # monitoring
    # debugging
    # business rules
    # encryption
"""

import functools

def memoize(fn):
    cache = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return memoizer

@memoize
def number_sum(n):
    assert (n >= 0), "n >= 0"
    if n == 0:
        return 0
    else:
        return n + number_sum(n-1)


@memoize
def fibonacci(n):
    assert (n>=0), "n >= 0"
    if n in (0,1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main():
    from timeit import Timer

    to_execute = [
        (number_sum,
         Timer('number_sum(300)', 'from __main__ import number_sum')),
        (fibonacci,
         Timer('fibonacci(100)', 'from __main__ import fibonacci'))
    ]

    for item in to_execute:
        fn = item[0]
        t = item[1]
        print(f"Time: {t.timeit()}")

if __name__ == "__main__":
    main()