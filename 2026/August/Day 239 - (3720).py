# 3720. Lexicographically Smallest Permutation Greater Than Target

# You are given two strings s and target, both having length n, consisting of lowercase English letters.
# Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.
# A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

# Example 1:
# Input: s = "abc", target = "bba"
# Output: "bca"
# Explanation:
# The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
# The lexicographically smallest permutation that is strictly greater than target is "bca".

# Example 2:
# Input: s = "leet", target = "code"
# Output: "eelt"
# Explanation:
# The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
# The lexicographically smallest permutation that is strictly greater than target is "eelt".

# Example 3:
# Input: s = "baba", target = "bbaa"
# Output: ""
# Explanation:
# The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
# None of them is lexicographically strictly greater than target. Therefore, the answer is "".

# Constraints:
# 1 <= s.length == target.length <= 300
# s and target consist of only lowercase English letters.

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        s_count = Counter(s)
        
        # Try finding a common prefix of length L (from longest possible down to 0)
        for L in range(n, -1, -1):
            # Verify if s has enough characters to match target[:L]
            prefix_count = Counter(target[:L])
            if any(s_count[ch] < prefix_count[ch] for ch in prefix_count):
                continue
            
            # Remaining characters available after matching target[:L]
            rem_count = s_count - prefix_count
            
            # If we matched the entire target (L == n), no strictly greater string can be formed from this prefix
            if L == n:
                continue
            
            # Find the smallest character strictly greater than target[L]
            target_char = target[L]
            next_char = None
            for ch in sorted(rem_count.keys()):
                if ch > target_char and rem_count[ch] > 0:
                    next_char = ch
                    break
            
            if next_char:
                # Use next_char at index L
                rem_count[next_char] -= 1
                
                # Build remaining part in ascending order
                suffix = []
                for ch in sorted(rem_count.keys()):
                    suffix.append(ch * rem_count[ch])
                
                return target[:L] + next_char + "".join(suffix)
                
        return ""

'''
so close to the deadline, so I used Gemini.ai for assistance to keep the streak. But a full review will come tomorrow
with an understanding of the problem and a more optimised solution.
'''