# 3713. Longest Balanced Substring I

# You are given a string s consisting of lowercase English letters.
# A substring of s is called balanced if all distinct characters in the substring appear
# the same number of times.
# Return the length of the longest balanced substring of s.

# Example 1:
# Input: s = "abbac"
# Output: 4
# Explanation:
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:
# Input: s = "zzabccy"
# Output: 4
# Explanation:
# The longest balanced substring is "zabc" because the distinct characters 'z', 'a', 'b', and 'c' each appear exactly 1 time.​​​​​​​

# Example 3:
# Input: s = "aba"
# Output: 2
# Explanation:
# ​​​​​​​One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

# Constraints:
# 1 <= s.length <= 1000
# s consists of lowercase English letters.

class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        n = len(s)

        # Get all unique characters in string
        unique_chars = set(s)
        
        # Brute force over substrings
        for i in range(n):
            # Reset dictionary for each starting position
            my_dict = {char: 0 for char in unique_chars}
            
            for j in range(i, n):
                # Add current character to count
                letter = s[j]
                my_dict[letter] += 1
                
                # Check if balanced
                # All values > 0 should be the same
                positive_vals = [v for v in my_dict.values() if v > 0]
                all_same = len(set(positive_vals)) <= 1
                
                if all_same and len(positive_vals) > 0:
                    max_length = max(max_length, j - i + 1)
        
        return max_length
    
    #same aproachas that for Day 41