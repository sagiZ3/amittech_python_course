def func1():
    sum = 0

    for i in range(1, 11):
        sum += i

    return sum


def main():
    x = func1()
    print(x)


if __name__ == '__main__':
    main()
