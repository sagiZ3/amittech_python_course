def print_instructions() -> None:
    instructions = ('instructions, enter:\n'
                    'r: read - for reading all usernames and passwords\n'
                    'rs: read specific - for reading a specific username and password\n'
                    'a: append - for adding an username and password\n'
                    'd: delete - for deleting all content in the file\n'
                    'q: quit - for exit from the system\n')
    print(instructions)

def main():
    try:
        open('password_manager.txt', 'x').close()
    except FileExistsError:
        pass

    print_instructions()

    while (action := input("What would you like to do: ")) != 'q':
        match action:
            case 'r':
                with open('password_manager.txt', 'r') as file:
                    print(file.read())

            case 'rs':
                requested_username = input('Enter username to search: ')

                with open('password_manager.txt', 'r') as file:
                    found = False
                    for item in file:
                        username = item.split(": ", 1)[0]
                        if username == requested_username:
                            found = True
                            print(f'Item found.\n{item}')
                            break

                if not found:
                    print('Item not found.')

            case 'a':
                username, password = input('Enter the username and password you want to append: ').split()
                with open('password_manager.txt', 'a') as file:
                    file.write(f'{username}: {password}\n')
                print('Username and password saved successfully!')

            case 'd':
                with open('password_manager.txt', 'w') as file:
                    file.write('')
                print('File content deleted successfully')
            case _:
                print('Invalid operation\nPlease follow the instructions above and try again.')


if __name__ == '__main__':
    main()
