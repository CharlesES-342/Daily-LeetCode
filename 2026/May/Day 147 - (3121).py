# 3121. Count the Number of Special Characters II

# You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
# Return the number of special letters in word.

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3
# Explanation:
# The special characters are 'a', 'b', and 'c'.

# Example 2:
# Input: word = "abc"
# Output: 0
# Explanation:
# There are no special characters in word.

# Example 3:
# Input: word = "AbBCab"
# Output: 0
# Explanation:
# There are no special characters in word.

# Constraints:
# 1 <= word.length <= 2 * 105
# word consists of only lowercase and uppercase English letters.

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        # last occurrence of lowercase letters
        last_lower = {}
        # first occurrence of uppercase letters
        first_upper = {}
        
        for i, char in enumerate(word):
            if char.islower():
                last_lower[char] = i
            elif char.isupper():
                if char not in first_upper: # only store first occurence
                    first_upper[char] = i
        
        count = 0
        for char in last_lower:
            upper_char = char.upper()
            # check if there is a fulfilling case
            if upper_char in first_upper and last_lower[char] < first_upper[upper_char]:
                count += 1
                
        return count