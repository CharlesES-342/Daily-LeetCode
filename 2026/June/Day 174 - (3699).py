# 3699. Number of ZigZag Arrays I

# You are given three integers n, l, and r.
# A ZigZag array of length n is defined as follows:
# Each element lies in the range [l, r].
# No two adjacent elements are equal.
# No three consecutive elements form a strictly increasing or strictly decreasing sequence.
# Return the total number of valid ZigZag arrays.
# Since the answer may be large, return it modulo 109 + 7.
# A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
# A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

# Example 1:
# Input: n = 3, l = 4, r = 5
# Output: 2
# Explanation:
# There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:
# [4, 5, 4]
# [5, 4, 5]​​​​​​​

# Example 2:
# Input: n = 3, l = 1, r = 3
# Output: 10
# Explanation:
# There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:
# [1, 2, 1], [1, 3, 1], [1, 3, 2]
# [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
# [3, 1, 2], [3, 1, 3], [3, 2, 3]
# All arrays meet the ZigZag conditions.

# Constraints:
# 3 <= n <= 2000
# 1 <= l < r <= 2000

class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1
        
        # dp0[j] -> Number of valid sequences ending at index j where the last move was DOWN (dir=0)
        # dp1[j] -> Number of valid sequences ending at index j where the last move was UP (dir=1)
        # Base case: For length 1, every element has exactly 1 valid configuration.
        dp0 = [1] * m
        dp1 = [1] * m
        
        # Transition from length 2 up to n (n-1 iterations)
        for _ in range(1, n):
            # Compute prefix sums for both arrays to achieve O(1) state transitions
            pref0 = [0] * (m + 1)
            pref1 = [0] * (m + 1)
            
            s0 = 0
            s1 = 0
            for j in range(m):
                s0 = (s0 + dp0[j]) % MOD
                pref0[j + 1] = s0
                
                s1 = (s1 + dp1[j]) % MOD
                pref1[j + 1] = s1
            
            # Vectorised updates using list comprehensions to prevent TLE
            # dp0[j] = sum(dp1[k]) for k > j
            next_dp0 = [(pref1[m] - pref1[j + 1]) % MOD for j in range(m)]
            # dp1[j] = sum(dp0[k]) for k < j
            next_dp1 = [pref0[j] for j in range(m)]
            
            # Roll over the arrays to the next position
            dp0 = next_dp0
            dp1 = next_dp1
            
        # Total valid sequences of length n is the combined sum of both final states
        return (sum(dp0) + sum(dp1)) % MOD
    
'''
I understand all outlined principles and applied my thought process. I didnt want to do the typing
so i gave my ideas to gemini. It took them, altered them and thorught it knew better (it didnt haha).
I went back and re-enforced my ideas so that it would not give me a solution that was not optimal.
'''