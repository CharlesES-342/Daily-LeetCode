# 3130. Find All Possible Stable Binary Arrays II

# You are given 3 positive integers zero, one, and limit.
# A binary array arr is called stable if:
# The number of occurrences of 0 in arr is exactly zero.
# The number of occurrences of 1 in arr is exactly one.
# Each subarray of arr with a size greater than limit must contain both 0 and 1.
# Return the total number of stable binary arrays.
# Since the answer may be very large, return it modulo 109 + 7.

# Example 1:
# Input: zero = 1, one = 1, limit = 2
# Output: 2
# Explanation:
# The two possible stable binary arrays are [1,0] and [0,1].

# Example 2:
# Input: zero = 1, one = 2, limit = 1
# Output: 1
# Explanation:
# The only possible stable binary array is [1,0,1].

# Example 3:
# Input: zero = 3, one = 3, limit = 2
# Output: 14
# Explanation:
# All the possible stable binary arrays are [0,0,1,0,1,1], [0,0,1,1,0,1], [0,1,0,0,1,1], [0,1,0,1,0,1], [0,1,0,1,1,0], [0,1,1,0,0,1], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,1,1,0], [1,0,1,0,0,1], [1,0,1,0,1,0], [1,0,1,1,0,0], [1,1,0,0,1,0], and [1,1,0,1,0,0].

# Constraints:
# 1 <= zero, one, limit <= 1000

'''
The exact same code as yesterdays problem as it was efficent enough from yesterday
'''
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
        """
        :type zero: int
        :type one: int
        :type limit: int
        :rtype: int
        """
        #given a number of 0's and 1's, howmany combinations are there where given any subarray there are
        # you also cannot have more than 'limit' number of 0's or 1's next to eachother
        
        #go though and form all of the valid arrays
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases: only 0s placed (j=0), up to limit consecutive 0s
        for i in range(min(zero, limit) + 1):
            dp0[i][0] = 1

        # Base cases: only 1s placed (i=0), up to limit consecutive 1s
        for j in range(min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(1, zero + 1):
            for j in range(1, one + 1):
                # Transition for dp0[i][j]: last element is 0
                dp0[i][j] = (dp1[i-1][j] + dp0[i-1][j]) % MOD
                if i > limit:
                    # Subtract schemes where previous `limit` elements were
                    # all 0s too — those had a 1 before that block
                    dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j]) % MOD

                # Transition for dp1[i][j]: last element is 1
                dp1[i][j] = (dp0[i][j-1] + dp1[i][j-1]) % MOD
                if j > limit:
                    # Subtract schemes where previous `limit` elements were
                    # all 1s too — those had a 0 before that block
                    dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD
        