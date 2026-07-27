def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def get_primes_till_n(n: int):
    for i in range(n + 1):
        if is_prime(i):
            yield i

def main():
    n = 10000
    for num in get_primes_till_n(n):
        print(num)


if __name__ == '__main__':
    main()
