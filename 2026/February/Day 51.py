# 761. Special Binary String

# Special binary strings are binary strings with the following two properties:
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# You are given a special binary string s.
# A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping
# them. Two strings are consecutive if the last character of the first string is exactly one index
# before the first character of the second string.
# Return the lexicographically largest resulting string possible after applying the mentioned
# operations on the string.


# Example 1:
# Input: s = "11011000"
# Output: "11100100"
# Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
# This is the lexicographically largest string possible after some number of swaps.

# Example 2:
# Input: s = "10"
# Output: "10"

# Constraints:
# 1 <= s.length <= 50
# s[i] is either '0' or '1'.
# s is a special binary string.


class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        #treat as the same problem as haveing valid ( and )
        #1. split into components (1=+1, 0=-1) a component is a balanced (sum = 0)
        #2. look insides, remove the outer 1 and 0
        #3. with this inner string, split this into components
        #4. sort the components to have the largest valid component at the frount, and so on
        #5. re-combine with the pervious outside substring

        #base case - if empty or short, return
        if not s:
            return ""

        res = []
        anchor = 0
        balance = 0
        
        #split the string into its "Special" components
        for i, char in enumerate(s):
            #step 1: 1 = +1, 0 = -1
            balance += 1 if char == '1' else -1
            
            #balance = 0 -> complete special substring
            if balance == 0:
                #RECURSIVELY:
                #step 2: remove the outer 1 and 0.
                inner_part = s[anchor + 1 : i]
                #step 3: then perform the same balance checks inside this substring
                processed_inner = self.makeLargestSpecial(inner_part)
                #re-combine to inclide outside
                res.append("1" + processed_inner + "0")
                
                #move the anchor to the start of the next component (fufills teh adjcaent componenet part)
                anchor = i + 1
        
        #step 4: sort the substrings into the order to give the largest overall
        res.sort(reverse=True)
        
        #step 5: add together all of the substrings that were valid and now inorder to make the final solution
        return "".join(res)
        
# Initially I had a hard time wrapping my head around the question, and so i asked Gemini to
# re-phrase it. From there, I managed to figure it out. While the code is not mine, the idea
# mostly is. I wanted to go about solving it in a long way and not involve recusion
# but i was made aware that a recursive soltion existed that made more sense in heind-sight.
# While the code is not mine, the idea and structure is.