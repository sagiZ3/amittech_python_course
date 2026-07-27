def print_instructions() -> None:
    instructions = ('instructions, enter:\n'
                    'r: read - for reading all usernames and passwords\n'
                    'rs: read specific - for reading a specific username and password\n'
                    'a: append - for adding an username and password\n'
                    'q: quit - for exit from the system\n')
    print(instructions)

def add_user():
    username = input("Username: ")
    password = input("Password: ")

    with open("password_manager.txt", "a") as file:
        file.write(f"{username}: {password}\n")


def show_all():
    with open("password_manager.txt", "r") as file:
        print(file.read())


def show_user():
    username = input("Username: ")

    with open("password_manager.txt", "r") as file:
        for line in file:
            if line.startswith(f"{username}: "):
                print(line, end="")
                return

    print("User not found.")


def main():
    with open("password_manager.txt", "a"):
        pass

    print_instructions()

    actions = {
        "a": add_user,
        "r": show_all,
        "rs": show_user,
    }

    while True:
        action = input("Action: ")

        if action == "q":
            break

        func = actions.get(action)

        if func:
            func()
        else:
            print("Invalid action")


if __name__ == "__main__":
    main()