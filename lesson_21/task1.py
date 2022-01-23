import time


class File:
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.start_time = time.time()
        self.file_obj = open(self.file_path, mode="w")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()
        print(time.time() - self.start_time)


if __name__ == '__main__':
    with File("hello.txt") as file:
        file.write("Hello, World!")
