import threading


class Counter(threading.Thread):
    COUNTER = 0
    ROUNDS = 100000

    def run(self):
        for _ in range(self.ROUNDS):
            self.COUNTER += 1


if __name__ == '__main__':
    t = Counter()
    t.start()
    t.join()
    print(t.COUNTER)
