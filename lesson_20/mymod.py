import sys


def count_lines(file_name):
    with open(file_name) as f:
        f.seek(0)
        return len(f.readlines())


def count_chars(file_name):
    characters = 0
    with open(file_name) as f:
        f.seek(0)
        for line in f.readlines():
            characters += len(line.strip())
        return characters


def test():
    chars = count_chars(sys.argv[-1])
    lines = count_lines(sys.argv[-1])
    return f'Characters {chars}, lines {lines}'


if __name__ == '__main__':
    print(count_lines('mymod.py'))
    print(count_chars('mymod.py'))
    print(test())
