"""
x  = create a new file (fails if the file already exists)
r  = read the file (fails if the file doesn't exist)
w  = write to the file (truncates the file if it exists, creates it otherwise)
r+ = read and write (file must already exist)
w+ = read and write (truncates the file if it exists, creates it otherwise)
a  = append to the file (creates the file if it doesn't exist)
a+ = read and append (creates the file if it doesn't exist)
"""

import msvcrt

def main():
    with open("test.txt", "w+", encoding='utf-8') as file:
        file.write("Hello - עברית")
        file.seek(0)
        print(file.read())
        print(file.fileno())
        file.seek(0)
        msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)  # No. represent bytes
        file.seek(0)
        with open("test.txt", "r", encoding='utf-8') as f:
            f.seek(1)
            print(f.read())

        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)

        with open("test.txt", "r", encoding='utf-8') as f:
            f.seek(0)
            print(f.read())

if __name__ == '__main__':
    main()
