y = 3
def one():
    # nonlocal y # fails too
    global y
    print(f'y = {y}')

    def two():
        nonlocal x
        print(f'x = {x}')

    two()
    x = 4

one()