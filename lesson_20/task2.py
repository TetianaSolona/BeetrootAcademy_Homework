import sys


class AddPath():
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        sys.path.insert(0, self.path)

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            sys.path.remove(self.path)
        except ValueError:
            pass


if __name__ == '__main__':
    with AddPath('pythonProject\\lesson_20'):
        print(sys.path)
