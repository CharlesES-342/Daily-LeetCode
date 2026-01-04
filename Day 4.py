#1390. Sum of Four Divisors

# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly 
# four divisors. If there is no such integer in the array, return 0.

 
# Example 1:
# Input: nums = [21,4,7]
# Output: 32
# Explanation: 
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.

# Example 2:
# Input: nums = [21,21]
# Output: 64

# Example 3:
# Input: nums = [1,2,3,4,5]
# Output: 0
 

# Constraints:

# 1 <= nums.length <= 104
# 1 <= nums[i] <= 105


#Version 1: Brute Force - Check each number for divisors

# class Solution(object):
#     def sumFourDivisors(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         def sum_of_divisors(n):
#             divisors = []
#             #goo though possible divisors up to sqrt(n)
#             for i in range(1, int(n**0.5) + 1):
#                 #if it is a divisor
#                 if n % i == 0:
#                     divisors.append(i)
#                     #check if it is not the square root to avoid adding twice
#                     if i != n // i:
#                         divisors.append(n // i)
#                 #if there are more than 4, stop checking
#                 if len(divisors) > 4:
#                     return 0
#             #if there are exactly 4 divisors, return their sum
#             if len(divisors) == 4:
#                 return sum(divisors)
#             return 0

#         #loop through each number in the list
#         total_sum = 0
#         for num in nums:
#             total_sum += sum_of_divisors(num)

#         return total_sum


#version 2: Optimized - CPT used to advance understanding and make it more effiencent (code still done by me)
class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def is_prime(n):
            if n < 2:
                return False
            for d in range(2, int(n**0.5) + 1):
                if n % d == 0:
                    return False
            return True

        totalSum = 0

        for num in nums:

            # ---------- Case 1: num = p^3 ----------
            # Use float only as an estimate, verify with integers
            p = int(num ** (1/3))
            if (p + 1) ** 3 == num:
                p += 1

            if p ** 3 == num and is_prime(p):
                totalSum += 1 + p + p*p + num
                continue

            # ---------- Case 2: num = p * q ----------
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    j = num // i
                    if i != j and is_prime(i) and is_prime(j):
                        totalSum += 1 + i + j + num
                    break   # only one factor pair needed

        return totalSum

