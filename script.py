from copy import deepcopy
from typing import Union


def add_two(num: Union[int, str, set]) -> int:
    if isinstance(num, str):
        return f"{num} + 2"
    elif isinstance(num, set):
        num.add(2)
        return num

    return num + 2


def main():
    x = 10
    y = add_two(x)

    print(x, y)

    x = "foo"
    y = add_two(x)
    print(x, y)

    x = set()
    y = add_two(deepcopy(x))

    print(x, y)


if __name__ == '__main__':
    main()
