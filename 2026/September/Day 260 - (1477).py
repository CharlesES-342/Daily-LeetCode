# 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

# You are given an array of integers arr and an integer target.
# You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.
# Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

# Example 1:
# Input: arr = [3,2,2,4,3], target = 3
# Output: 2
# Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.

# Example 2:
# Input: arr = [7,3,4,7], target = 7
# Output: 2
# Explanation: Although we have three non-overlapping sub-arrays of sum = 7 ([7], [3,4] and [7]), but we will choose the first and third sub-arrays as the sum of their lengths is 2.

# Example 3:
# Input: arr = [4,3,2,6,2,3,4], target = 6
# Output: -1
# Explanation: We have only one sub-array of sum = 6.

# Constraints:
# 1 <= arr.length <= 105
# 1 <= arr[i] <= 1000
# 1 <= target <= 108

class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        min_len = [float("inf")] * n

        left = 0
        current_sum = 0
        best_single_len = float("inf")
        ans = float("inf")

        for i in range(n):
            current_sum += arr[i]

            # Shrink window if current sum exceeds target
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            # Found a valid sub-array ending at this index
            if current_sum == target:
                curr_len = i - left + 1

                # If there is a valid sub-array before it (no overlapping)
                if left > 0 and min_len[left - 1] != float("inf"):
                    ans = min(ans, curr_len + min_len[left - 1])

                best_single_len = min(best_single_len, curr_len)

            # Update the minimum length up to current index
            min_len[i] = best_single_len

        return ans if ans != float("inf") else -1