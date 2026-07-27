def one():
    def two():
        nonlocal x
        print(f'x = {x}')

    x = 4
    two()

one()