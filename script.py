from copy import deepcopy
from typing import Union


def add_value(num, value):
    """A very large change happended here
    """
    return num + value


def main():
    x = 10
    v = 5
    y = add_value(x, v)

    print(x, v, y)

    x = "foo"
    y = add_value(x, "bar")
    print(x, y)


if __name__ == '__main__':
    main()
