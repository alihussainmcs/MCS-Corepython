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


def prime_check_req_gen(a1):
    for i in a1[1]:
        if a1[0] % i == 0:
            return False
    else:
        return True


# print(prime_check_req_gen(100, range(2, 50)))
# print(prime_check_req_gen(100, [2,5]))
num = 100
# while True:
#     pass
#     # c = 2
#     # d = b // 8
#     # p1 = mp.Process(target=prime_check_req_gen, args=(b, range(2, d)))
    # p2 = mp.Process(target=prime_check_req_gen, args=(b, a(d, d + d)))
    # p3 = mp.Process(target=prime_check_req_gen, args=(b, a(d + d, d + d + d)))
    # p4 = mp.Process(target=prime_check_req_gen, args=(b, a(d + d + d, d + d + d + d)))
    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # b += 1
    # p1.join()
    # p2.join()
    # p3.join()
    # p4.join()
    # print(p1.result())
pool = mp.Pool()
r = num//8
print(prime_check_req_gen([num, range(2, 50)]))
iter_list = [range(2, r), range(r, 2*r),range(2*r, 3*r),range(3*r, 4*r)]
result_list = pool.map(prime_check_req_gen, [[num, [i for i in range(2,50)]], [num, [i for i in range(2,50)]]])
# print(result_list)


