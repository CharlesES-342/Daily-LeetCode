# 835. Image Overlap

# You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.
# We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.
# Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.
# Return the largest possible overlap.

# Example 1:
# Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
# Output: 3
# Explanation: We translate img1 to right by 1 unit and down by 1 unit.
# The number of positions that have a 1 in both images is 3 (shown in red).

# Example 2:
# Input: img1 = [[1]], img2 = [[1]]
# Output: 1

# Example 3:
# Input: img1 = [[0]], img2 = [[0]]
# Output: 0

# Constraints:
# n == img1.length == img1[i].length
# n == img2.length == img2[i].length
# 1 <= n <= 30
# img1[i][j] is either 0 or 1.
# img2[i][j] is either 0 or 1.

from collections import Counter

class Solution(object):
    def largestOverlap(self, img1, img2):
        """
        :type img1: List[List[int]]
        :type img2: List[List[int]]
        :rtype: int
        """
        n = len(img1)
        
        # Collect coordinates of all 1s in img1 and img2
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        
        # Count translation vectors
        count = Counter()
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                count[(r2 - r1, c2 - c1)] += 1
                
        # Return the maximum overlap (0 if no 1s exist in either grid)
        return max(count.values()) if count else 0
    

'''
While intuative following the solution, I was initially stumped and inlisted the help og Gemini.ai
to help produce a solution.
This solution is based on teh idea of translation, for ever position in image1, the movement
to every position in image2 is considered, and for all the positions, the change (translation)
that is applied is counted. The more values that map to a matchin one given the same translation,
the better that translation is in producing the desired max-correspondance. The overall directions
are not required, only the change in location, therefore the translation vector (change in x and y)
is mroe than enough - this is stored as count(change in row, change in column).
Following completion, this is incredibly ovbious and has made me annoyed that I did not see it intialy.
While I knew the actual translation was not required (only the change), I am ashamed to say that I was
stumped on how to determine the most effective translation.
'''