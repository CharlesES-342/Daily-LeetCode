# 1871. Jump Game VII

# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

# Example 1:
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.

# Example 2:
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false

# Constraints:
# 2 <= s.length <= 105
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        # end is an bosticle and cant get there
        if s[n-1] == '1':
            return False
            
        dp = [False] * n
        dp[0] = True
        reachable_count = 0
        
        for i in range(1, n):
            # add the index that just entered the jump range
            if i >= minJump:
                if dp[i - minJump]:
                    reachable_count += 1
            
            # remove the index that just left the jump range
            if i > maxJump:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # if there is at least one reachable point in range and s[i] is '0'
            if reachable_count > 0 and s[i] == '0':
                dp[i] = True
                
        return dp[n-1]