# 2839. Check if Strings Can be Made Equal With Operations I

# You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.

# Example 1:
# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: We can do the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
# - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

# Example 2:
# Input: s1 = "abcd", s2 = "dacb"
# Output: false
# Explanation: It is not possible to make the two strings equal.

# Constraints:
# s1.length == s2.length == 4
# s1 and s2 consist only of lowercase English letters.

class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # just change one of the strings to make the other (no point doing it to both)
        # since it is only of length 4, there are only 2 possible swaps
        possible = False
        swap1 = s2[2]+s2[1]+s2[0]+s2[3] # 0 and 2 swapped
        swap2 = s2[0]+s2[3]+s2[2]+s2[1] # 1 and 3 swapped
        swap3 = s2[2]+s2[3]+s2[0]+s2[1] # 0 and 2 swapped + 1 and 3 swapped


        if s1 == s2 or s1 in (swap1, swap2, swap3):
            return True

        return False
        
        #could also consider checking that the elements in matching positions are matching
        #    for example:
        #       0 and 2 in s1 are the same as 0 and 2 in s2
        #       1 and 3 in s1 are the same as 1 and 3 in s2
        
class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return sorted([s1[0],s1[2]]) == sorted([s2[0],s2[2]]) and \
               sorted([s1[1],s1[3]]) == sorted([s2[1],s2[3]])
        