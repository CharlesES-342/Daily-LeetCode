# 1358. Number of Substrings Containing All Three Characters

# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

# Example 2:
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

# Example 3:
# Input: s = "abc"
# Output: 1

# Constraints:
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Array to track the last seen position of 'a', 'b', and 'c'
        # Index 0 -> 'a', Index 1 -> 'b', Index 2 -> 'c'
        last_seen = [-1, -1, -1]
        count = 0
        
        for r in range(len(s)):
            # Update the last seen index for the current character
            last_seen[ord(s[r]) - ord('a')] = r
            
            # If all three characters have been seen at least once,
            # any substring starting from index 0 up to min(last_seen) 
            # and ending at 'r' is valid.
            if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
                count += min(last_seen) + 1
                
        return count