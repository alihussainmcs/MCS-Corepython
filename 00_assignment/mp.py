# def print_prime_above(num):
#     for i in range(2, num // 2):
#         if num % i == 0:
#             return False
#     else:
#         return True
#
#
# a = 10000000
# while True:
#     if print_prime_above(a):
#         print(a)
#     a += 1

# -------------------------------------------------------------------------------------------------------

import multiprocessing as mp


def gen_range(start, end):
    for i in range(start, end):
        yield i


a = gen_range


def prime_check_req_gen(num, a1):
    for i in a1:
        if num % i == 0:
            return False
    else:
        return True


b = 10000000
while True:
    c = 2
    d = b // 8
    # p1 = mp.Process(target=prime_check_req_gen, args=(b, range(2, d)))
    # p2 = mp.Process(target=prime_check_req_gen, args=(b, a(d, d + d)))
    # p3 = mp.Process(target=prime_check_req_gen, args=(b, a(d + d, d + d + d)))
    # p4 = mp.Process(target=prime_check_req_gen, args=(b, a(d + d + d, d + d + d + d)))
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    b += 1
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    print(p1.result())
    pool = mp.Pool(processes=6)
    print(pool.map(prime_check_req_gen()))
