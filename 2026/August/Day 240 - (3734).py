# 3734. Lexicographically Smallest Palindromic Permutation Greater Than Target

# You are given two strings s and target, each of length n, consisting of lowercase English letters.
# Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

# Example 1:
# Input: s = "baba", target = "abba"
# Output: "baab"
# Explanation:
# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# The lexicographically smallest permutation that is strictly greater than target is "baab".

# Example 2:
# Input: s = "baba", target = "bbaa"
# Output: ""
# Explanation:
# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# None of them is lexicographically strictly greater than target. Therefore, the answer is "".

# Example 3:
# Input: s = "abc", target = "abb"
# Output: ""
# Explanation:
# s has no palindromic permutations. Therefore, the answer is "".

# Example 4:
# Input: s = "aac", target = "abb"
# Output: "aca"
# Explanation:
# The only palindromic permutation of s is "aca".
# "aca" is strictly greater than target. Therefore, the answer is "aca".

# Constraints:
# 1 <= n == s.length == target.length <= 300
# s and target consist of only lowercase English letters.

class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """:type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        s_count = Counter(s)
        
        # Can s form a palindrome
        odd_chars = [ch for ch in s_count if s_count[ch] % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        # get the middle character (if applicable)
        mid_char = odd_chars[0] if odd_chars else ""
        if odd_chars:
            s_count[mid_char] -= 1  # Temporarily remove this central character from the count pool
            if s_count[mid_char] == 0:
                del s_count[mid_char]

        # Focus on constructiung the first half
        # only use half of the characters to make it work
        half_count = {ch: s_count[ch] // 2 for ch in s_count}
        half_n = n // 2
        
        # Try finding a common prefix of length L for the first half (from longest down to 0)
        # Similar approach to the previous construction
        for L in range(half_n, -1, -1):
            prefix_count = Counter(target[:L])
            # Check if the available character pool has enough supplies to build this prefix slice of length L.
            if any(half_count.get(ch, 0) < prefix_count[ch] for ch in prefix_count):
                continue
            
            # Determine what character supplies remain after carving out the target prefix slice.
            rem_count = {ch: half_count.get(ch, 0) - prefix_count[ch] for ch in half_count}
            
            if L == half_n:
                # If the first half matches target[:half_n], check if the full palindrome is > target
                first_half = target[:half_n]
                candidate = first_half + mid_char + first_half[::-1]
                # Even if the first half matches, it might still fail the strict greater-than check.
                if candidate > target:
                    return candidate
                continue
            
            target_char = target[L]
            next_char = None
            # Scan all available remaining keys in alphabetical order to find the immediate next character choice that exceeds target[L].
            for ch in sorted(rem_count.keys()):
                if ch > target_char and rem_count[ch] > 0:
                    next_char = ch
                    break
            
            if next_char:
                rem_count[next_char] -= 1
                
                # Sort remaining character pool alphabetically so we can pack them into the smallest possible suffix ordering.
                suffix = []
                for ch in sorted(rem_count.keys()):
                    suffix.append(ch * rem_count[ch])
                
                # Assemble the first half: matched prefix + bumped next character + sorted remaining characters.
                first_half = target[:L] + next_char + "".join(suffix)
                # Mirror the constructed first half around the middle character to form the valid, strictly greater palindromic result.
                return first_half + mid_char + first_half[::-1]
                
        return ""