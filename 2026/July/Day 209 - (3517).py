# 3517. Smallest Palindromic Rearrangement I

# You are given a palindromic string s.
# Return the lexicographically smallest palindromic permutation of s.

# Example 1:
# Input: s = "z"
# Output: "z"
# Explanation:
# A string of only one character is already the lexicographically smallest palindrome.

# Example 2:
# Input: s = "babab"
# Output: "abbba"
# Explanation:
# Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

# Example 3:
# Input: s = "daccad"
# Output: "acddca"
# Explanation:
# Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

# Constraints:
# 1 <= s.length <= 105
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.

'''
Initial approach from my own understanding
'''
from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Count the occurrences of each character in the string
        counts = Counter(s)
        
        first_half = []
        mid_char = ""
        
        # Sort the unique characters lexicographically (alphabetically)
        for char in sorted(counts.keys()):
            count = counts[char]
            
            # Add half of the character's instances to the first half
            first_half.append(char * (count // 2))
            
            # If a character has an odd count, it must sit in the middle
            if count % 2 != 0:
                mid_char = char
        
        # Join the sorted first half elements together
        left = "".join(first_half)
        
        # Construct the final palindrome: left + middle + reversed(left)
        return left + mid_char + left[::-1]

'''
But another approach that should not necessarily work, but seems to:
'''
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        # Base Case: length <= 1, return the string as it is
        if n <= 1:
            return s
        
        # Get the sorted first half of the string
        sorted_half = sorted(s[:n // 2])
        
        # Identify the middle character if the length is odd
        mid_char = [s[n // 2]] if n % 2 else []
        
        # Construct the palindrome by combining: first_half + mid_char + reversed_first_half
        return "".join(sorted_half + mid_char + sorted_half[::-1])