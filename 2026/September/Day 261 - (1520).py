# 1520. Maximum Number of Non-Overlapping Substrings

# Given a string s of lowercase letters, you need to find the maximum number of non-empty substrings of s that meet the following conditions:
# The substrings do not overlap, that is for any two substrings s[i..j] and s[x..y], either j < x or i > y is true.
# A substring that contains a certain character c must also contain all occurrences of c.
# Find the maximum number of substrings that meet the above conditions. If there are multiple solutions with the same number of substrings, return the one with minimum total length. It can be shown that there exists a unique solution of minimum total length.
# Notice that you can return the substrings in any order.

# Example 1:
# Input: s = "adefaddaccc"
# Output: ["e","f","ccc"]
# Explanation: The following are all the possible substrings that meet the conditions:
# [
#   "adefaddaccc"
#   "adefadda",
#   "ef",
#   "e",
#   "f",
#   "ccc",
# ]
# If we choose the first string, we cannot choose anything else and we'd get only 1. If we choose "adefadda", we are left with "ccc" which is the only one that doesn't overlap, thus obtaining 2 substrings. Notice also, that it's not optimal to choose "ef" since it can be split into two. Therefore, the optimal way is to choose ["e","f","ccc"] which gives us 3 substrings. No other solution of the same number of substrings exist.

# Example 2:
# Input: s = "abbaccd"
# Output: ["d","bb","cc"]
# Explanation: Notice that while the set of substrings ["d","abba","cc"] also has length 3, it's considered incorrect since it has larger total length.

# Constraints:
# 1 <= s.length <= 105
# s contains only lowercase English letters.

class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # non-overlapping
        # all occurences of a letter must be mapped to the same array

        n = len(s)

        # for every character, determine the locations of the first and last letter
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i


        # for each character, then determine if there are any other characters in this range (add the new end index based on the contained characters)
        valid_intervals = []
        for ch in first:
            start = first[ch]
            end = last[ch]
            
            is_valid = True
            i = start
            while i <= end:
                # Expand boundaries if a character inside requires a wider range
                if first[s[i]] < start:
                    is_valid = False  # Extended past our start index
                    break
                end = max(end, last[s[i]])
                i += 1
                
            if is_valid:
                valid_intervals.append((end, start))

        # order the character start and end pointers based on length (output those which do not overlap based on the smallest order). This will form all of the smallest arrays with non-overlapping (or minimal overlapping) characters
        valid_intervals.sort()

        result = []
        prev_end = -1
        
        for end, start in valid_intervals:
            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end
                
        return result