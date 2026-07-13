# 1189. Maximum Number of Balloons

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

# Constraints:
# 1 <= text.length <= 104
# text consists of lower case English letters only.

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # since order does not matter, only count, find the smallest mutiple of each other the nimber for required letters
        # Requirements for "balloon": b=1, a=1, l=2, o=2, n=1
        multiple = [1, 1, 2, 2, 1]
        found = [0, 0, 0, 0, 0]
        
        for i in text:
            if i == 'b':
                found[0] += 1
            elif i == 'a':
                found[1] += 1
            elif i == 'l':
                found[2] += 1
            elif i == 'o':
                found[3] += 1
            elif i == 'n':
                found[4] += 1

        return min(found[n] // multiple[n] for n in range(5))
    

    '''
    Which can be simplified to:
    '''

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        b=text.count('b')
        a=text.count('a')
        l=text.count('l')//2
        o=text.count('o')//2
        n=text.count('n')
        return min(b,a,l,o,n)