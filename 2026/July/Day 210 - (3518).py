# 3518. Smallest Palindromic Rearrangement II

# You are given a palindromic string s and an integer k.
# Return the k-th lexicographically smallest palindromic permutation of s. If there are fewer than k distinct palindromic permutations, return an empty string.
# Note: Different rearrangements that yield the same palindromic string are considered identical and are counted once.

# Example 1:
# Input: s = "abba", k = 2
# Output: "baab"
# Explanation:
# The two distinct palindromic rearrangements of "abba" are "abba" and "baab".
# Lexicographically, "abba" comes before "baab". Since k = 2, the output is "baab".

# Example 2:
# Input: s = "aa", k = 2
# Output: ""
# Explanation:
# There is only one palindromic rearrangement: "aa".
# The output is an empty string since k = 2 exceeds the number of possible rearrangements.

# Example 3:
# Input: s = "bacab", k = 1
# Output: "abcba"
# Explanation:
# The two distinct palindromic rearrangements of "bacab" are "abcba" and "bacab".
# Lexicographically, "abcba" comes before "bacab". Since k = 1, the output is "abcba".

# Constraints:
# 1 <= s.length <= 104
# s consists of lowercase English letters.
# s is guaranteed to be palindromic.
# 1 <= k <= 106


import collections

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        MAX_VAL = 10**6 + 1   

        # Determine character frequencies
        frequencies = collections.Counter(s)

        # Check if a palindrome is possible
        odd_count = sum(1 for freq in frequencies.values() if freq % 2 == 1)
        if odd_count > 1:
            return ""

        # Only look at the half array (just the beginning as the rest is the reverse)
        half_count = [0] * 26
        mid_letter = ""
        for char, freq in frequencies.items():
            idx = ord(char) - ord('a')
            half_count[idx] = freq // 2
            if freq % 2 == 1:
                mid_letter = char

        # Helper to compute combinations (multinomial coefficients)
        def count_arrangements(counts):
            total = sum(counts)
            res = 1
            for freq in counts:
                if freq == 0:
                    continue
                # Calculate combinations using math.comb or iterative multiplication
                comb = 1
                for i in range(1, min(freq, total - freq) + 1):
                    comb = comb * (total - i + 1) // i
                    if comb >= MAX_VAL:
                        return MAX_VAL
                res *= comb
                if res >= MAX_VAL:
                    return MAX_VAL
                total -= freq
            return res


        # Check if total permutations are enough to reach k (if not, return an empty string)
        total_perms = count_arrangements(half_count)
        if k > total_perms:
            return ""

        # Incrementally choose each character from smallest to largest
        half_len = sum(half_count)
        left_half = []
        
        for _ in range(half_len):
            for i in range(26):
                if half_count[i] == 0:
                    continue
                
                # Try placing the character at the current position
                half_count[i] -= 1
                arrangements = count_arrangements(half_count)
                
                # If count is at least k, fix that character
                if arrangements >= k:
                    left_half.append(chr(i + ord('a')))
                    break
                else:
                    # Otherwise, subtract the count from k and try the next candidate
                    k -= arrangements
                    half_count[i] += 1
                    
        left_str = "".join(left_half)
        return left_str + mid_letter + left_str[::-1]