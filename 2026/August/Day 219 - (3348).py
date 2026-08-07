# 3348. Smallest Divisible Digit Product II

# You are given a string num which represents a positive integer, and an integer t.
# A number is called zero-free if none of its digits are 0.
# Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

# Example 1:
# Input: num = "1234", t = 256
# Output: "1488"
# Explanation:
# The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

# Example 2:
# Input: num = "12355", t = 50
# Output: "12355"
# Explanation:
# 12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

# Example 3:
# Input: num = "11111", t = 26
# Output: "-1"
# Explanation:
# No number greater than 11111 has the product of its digits divisible by 26.

# Constraints:
# 2 <= num.length <= 2 * 105
# num consists only of digits in the range ['0', '9'].
# num does not contain leading zeros.
# 1 <= t <= 1014

class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        temp = t
        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)
        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1

        num_list = list(num)
        for i in range(n):
            if num_list[i] == "0":
                pos = i
                break
            rem[i + 1] = rem[i] // gcd(rem[i], int(num_list[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):
            while True:
                num_list[i] = chr(ord(num_list[i]) + 1)
                if num_list[i] > "9":
                    break

                t_now = rem[i] // gcd(rem[i], int(num_list[i]))
                k = 9

                for j in range(n - 1, i, -1):
                    while t_now % k != 0:
                        k -= 1
                    t_now //= k
                    num_list[j] = str(k)

                if t_now == 1:
                    return "".join(num_list)

        ans = []
        original_t = t
        for i in range(9, 1, -1):
            while original_t % i == 0:
                ans.append(str(i))
                original_t //= i

        ans_str = "".join(ans)
        padding = max(n + 1 - len(ans_str), 0)
        ans_str += "1" * padding

        return ans_str[::-1]


'''
Made use of Gemini.ai and the editorial.
How it works...
Since T can only have prime factors of 2,3,5 and 7 (due to it being all the primes in 0-9 formed
using the product of the digits), we can check if it is poossibhle initially. If other prime
factors are in the number, then it is not-possible -> return "-1".

Then find the number that satisfied the whole thing.
This is done by checking the number from the end, and if it is not possible to make a number
with the current digit, then we increment the digit and try again. If we reach 9, then we move to
the next digit and repeat. This is reduced as rather than +1 and converting back to a string and
then to a number again, you can just move through the string array. 
'''