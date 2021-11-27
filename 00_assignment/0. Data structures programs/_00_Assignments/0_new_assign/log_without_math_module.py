def log(x, base):
    log_b = 2
    while x != int(round(base ** log_b)):
        log_b += 0.12
        # print(log_b)
    return log_b  # """int(round(log_b))"""


# log(10,10)
print(log(10, 2))
print(log(9, 2))
print(log(8, 2))
print(log(7, 2))
