# 3863. Minimum Operations to Sort a String

# You are given a string s consisting of lowercase English letters.
# In one operation, you can select any substring of s that is not the entire string and sort it in non-descending alphabetical order.
# Return the minimum number of operations required to make s sorted in non-descending order. If it is not possible, return -1.

# Example 1:
# Input: s = "dog"
# Output: 1
# Explanation:​​​​​​​
# Sort substring "og" to "go".
# Now, s = "dgo", which is sorted in ascending order. Thus, the answer is 1.

# Example 2:
# Input: s = "card"
# Output: 2
# Explanation:
# Sort substring "car" to "acr", so s = "acrd".
# Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending order. Thus, the answer is 2.

# Example 3:
# Input: s = "gf"
# Output: -1
# Explanation:
# It is impossible to sort s under the given constraints. Thus, the answer is -1.

# Constraints:
# 1 <= s.length <= 105
# s consists of only lowercase English letters.

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        # the answer will either be -1, 0, 1, 2 or 3 (as you can ake all elemets except the final, sort, and then take all except the first and sort, then sort the items in index 0 and 1)
        n = len(s)

        # Check if initial array is sorted
        if s == "".join(sorted(s)):
            return 0
        else:
            # too short to be sorted without overlap
            if n <=2:
                return -1

            mn = min(s)
            mx = max(s)
            # all orientations must be looked at otherwise you wont necessarily get the minimum number of sorts

            # Case: 1 sort
            # 1. first n-2 elements sorted
            # 2. last n-2 elemets sorted
            if s[0] == mn or s[-1] == mx:
                return 1

            # Case: 3 sorts required
            # the joining edge cases need to be checked (the new character introduces from the 2nd swap may not fit with the character not looked at)
            # 1. dort the first 2 elemets
            # 2. sort the bast 2 elements
            if s[0] == mx and s[-1] == mn and s.count(mx) == 1 and s.count(mn) == 1:
                return 3

            # Case: 2 sorts - if required, the order of these matters!
            # from each of these above, swap the other ends too
            # 1. last n-2 elemets sorted
            # 2. first n-2 elemets sorted

            for i in range(1, n - 1):
                if s[i] == mn or s[i] == mx:
                    return 2
                
        return 3