def main():
    print(globals())
    print(__file__)

    globals()['x'] = 1
    print(f'x = {x}')


if __name__ == '__main__':
    print('NOT Awesome')
    __name__ = 'wow'
    print()

if __name__ == 'wow':
    print('Awesome!!!')
    main()
