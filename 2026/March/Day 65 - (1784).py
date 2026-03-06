# 1784. Check if Binary String Has at Most One Segment of Ones
# Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

# Example 1:
# Input: s = "1001"
# Output: false
# Explanation: The ones do not form a contiguous segment.

# Example 2:
# Input: s = "110"
# Output: true

# Constraints:
# 1 <= s.length <= 100
# s[i]​​​​ is either '0' or '1'.
# s[0] is '1'.

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        segment = False
        found = False 
        for i in s:
            if i == '1' and not found:
                found = True
            elif i =='0' and found:
                segment = True
            elif i == '1' and segment:
                return False
        return True
        