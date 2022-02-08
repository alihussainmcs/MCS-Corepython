from multiprocessing import Pool


def is_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    numbers = range(1000)
    pool = Pool(processes=4)
    # while True:
    print(pool.map(is_prime, numbers))
