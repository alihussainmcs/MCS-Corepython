# from multiprocessing import Pool
# 
# 
# def is_prime(number):
#     if number == 2 or number == 3:
#         return True
#     if number % 2 == 0 or number < 2:
#         return False
#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True
# 
# 
# if __name__ == '__main__':
#     numbers = range(1000)
#     pool = Pool(processes=4)
#     # while True:
#     print(pool.map(is_prime, numbers))

class Solution:
    @staticmethod
    def isMonotonic(nums):
        a = nums[0]

        b = nums[1]
        print(b)
        if a > b: #decreasing
            for index, value in enumerate(nums[:-2]):
                print(value, index)
                if value > nums[index+1]:
                    return False
            else:
                return True
        elif a < b:
            for index, value in enumerate(nums[:-2]):
                if value < nums[index+1]:
                    print(value, index)
                    return False
            else:
                return True


num = [1,3,2]
l1 =[4,3,2]

print(Solution.isMonotonic(l1))