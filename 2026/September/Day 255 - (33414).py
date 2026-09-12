# 3414. Maximum Score of Non-overlapping Intervals

# You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.
# Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.
# Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

# Example 1:
# Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]
# Output: [2,3]
# Explanation:
# You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

# Example 2:
# Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]
# Output: [1,3,5,6]
# Explanation:
# You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

# Constraints:
# 1 <= intevals.length <= 5 * 104
# intervals[i].length == 3
# intervals[i] = [li, ri, weighti]
# 1 <= li <= ri <= 109
# 1 <= weighti <= 109


from bisect import bisect_left


class Solution(object):

  def maximumWeight(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[int]
    """
    n = len(intervals)

    # Sort indices based on right boundary (intervals[i][1])
    order = sorted(range(n), key=lambda i: intervals[i][1])

    # Array of sorted right boundaries for binary search
    rights = [intervals[i][1] for i in order]

    # Base state for 0 intervals picked: (score_negated, sorted_indices_list)
    # select maximum score,
    # and breaks ties using lexicographically smallest original index list.
    prev = [(0, [])] * (n + 1)

    # DP over picking at most 4 intervals
    for _ in range(4):
      cur = [(0, [])] * (n + 1)
      for p in range(1, n + 1):
        idx = order[p - 1]
        l, r, w = intervals[idx]

        # Find the number of intervals ending strictly before l
        j = bisect_left(rights, l)

        score, ids = prev[j]
        # Option 1: Include interval `idx`
        # Option 2: Exclude interval `idx` (take cur[p - 1])
        cur[p] = min((score - w, sorted(ids + [idx])), cur[p - 1])

      prev = cur

    return prev[n][1]

'''
By sorting by right intervals, the intervals what can strictly end before this index are processed
already..
Therefore, those with any boundary less than this index are struictly going to occure on the left
of this index.

cur[p] is th eoptimal choice
for each interva l(p) there are 2 options:
    Exclude P: take the best up to p1
    Inclide p: combine the interval p wiht the best result from before p (which is prev[j] where j
            is the index of the last interval that ends before l)

Handelling tie breakers: maximise the score and minuimise the lexicographically smallest index
list.
min((score - w, sorted(ids + [idx])), cur[p - 1]) uses negated score (score - w)
If the weights are the same it falls back on "sorted(ids + [idx])" to select the maller one
lexecographically.
'''