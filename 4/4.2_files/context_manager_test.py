import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.perf_counter() - self.start
        print(f"Took {elapsed:.3f} seconds")


def main():
    with Timer():
        sum(range(10_000_000))


if __name__ == '__main__':
    main()
