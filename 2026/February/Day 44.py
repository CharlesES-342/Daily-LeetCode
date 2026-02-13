# 3714. Longest Balanced Substring II

# You are given a string s consisting only of the characters 'a', 'b', and 'c'.
# A substring of s is called balanced if all distinct characters in the substring appear the same number of times.
# Return the length of the longest balanced substring of s.

# Example 1:
# Input: s = "abbac"
# Output: 4
# Explanation:
# The longest balanced substring is "abba" because both distinct characters 'a' and 'b' each appear exactly 2 times.

# Example 2:
# Input: s = "aabcc"
# Output: 3
# Explanation:
# The longest balanced substring is "abc" because all distinct characters 'a', 'b' and 'c' each appear exactly 1 time.

# Example 3:
# Input: s = "aba"
# Output: 2
# Explanation:
# One of the longest balanced substrings is "ab" because both distinct characters 'a' and 'b' each appear exactly 1 time. Another longest balanced substring is "ba".

# Constraints:
# 1 <= s.length <= 105
# s contains only the characters 'a', 'b', and 'c'.

class Solution(object):
    def longestBalanced(self, s):
        """
        Find the length of the longest balanced substring.
        A substring is balanced if all characters present have equal counts.
        """
        n = len(s)
        if n == 0:
            return 0
        
        max_len = 0
        
        #Case 1: exactly 1 distinct character
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            max_len = max(max_len, j - i)
            i = j
        
        #Case 2: exactly 2 distinct characters
        #for each pair of characters, find longest substring where both have equal count
        for char1 in ['a', 'b', 'c']:
            for char2 in ['a', 'b', 'c']:
                if char1 >= char2:
                    continue
                
                # Use prefix difference technique
                diff_map = {0: -1}  # difference -> earliest index
                count1, count2 = 0, 0
                
                for idx in range(n):
                    if s[idx] == char1:
                        count1 += 1
                    elif s[idx] == char2:
                        count2 += 1
                    else:
                        #reset when we see a third character
                        diff_map = {0: idx}
                        count1, count2 = 0, 0
                        continue
                    
                    diff = count1 - count2
                    
                    if diff in diff_map:
                        length = idx - diff_map[diff]
                        max_len = max(max_len, length)
                    else:
                        diff_map[diff] = idx
        
        #Case 3: exactly 3 distinct characters (a, b, c)
        #use two differences: (count_b - count_a, count_c - count_a)
        pair_map = {(0, 0): -1}
        count_a, count_b, count_c = 0, 0, 0
        
        for idx in range(n):
            if s[idx] == 'a':
                count_a += 1
            elif s[idx] == 'b':
                count_b += 1
            else:  # 'c'
                count_c += 1
            
            pair = (count_b - count_a, count_c - count_a)
            
            if pair in pair_map:
                length = idx - pair_map[pair]
                max_len = max(max_len, length)
            else:
                pair_map[pair] = idx
        
        return max_len