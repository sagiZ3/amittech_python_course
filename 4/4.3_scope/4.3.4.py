def show_scope(num: int) -> None:
    num2 = 3
    name = 'Sagi'
    scope = 'function local'

    print(locals())


def main():
    print('locals:')
    show_scope(8)
    print('globals:')
    print(globals())


if __name__ == '__main__':
    main()
