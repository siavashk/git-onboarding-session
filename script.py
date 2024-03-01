def add_value(num: int, value: int) -> int:
    if not isinstance(value, int):
        raise ValueError(f"Error: only integer values are supported got {value}")

    if not isinstance(num, int):
        raise ValueError(f"Error: only integer values are supported got {num}")

    if value == 2:
        return num + 4
    elif value == 5:
        return num + 2 * value
    else:
        return num + value


def main():
    x = 10
    v = 5
    y = add_value(x, v)

    print(x, v, y)


if __name__ == '__main__':
    main()
