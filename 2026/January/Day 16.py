# 2975. Maximum Square Area by Removing Fences From a Field

# There is a large (m - 1) x (n - 1) rectangular field with corners at (1, 1) and (m, n) containing some horizontal and vertical
# fences given in arrays hFences and vFences respectively.

# Horizontal fences are from the coordinates (hFences[i], 1) to (hFences[i], n) and vertical fences are from the coordinates (1,
# vFences[i]) to (m, vFences[i]).

# Return the maximum area of a square field that can be formed by removing some fences (possibly none) or -1 if it is impossible
# to make a square field.

# Since the answer may be large, return it modulo 109 + 7.

# Note: The field is surrounded by two horizontal fences from the coordinates (1, 1) to (1, n) and (m, 1) to (m, n) and two vertical
# fences from the coordinates (1, 1) to (m, 1) and (1, n) to (m, n). These fences cannot be removed.

class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        
        #boundaries to fence lists
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        hFences.sort()
        vFences.sort()

        #get possible differences in the array (horizontal)
        h_distances = set()
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                h_distances.add(hFences[j] - hFences[i])
        
        #get possible differences in the array (vertical)
        v_distances = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                v_distances.add(vFences[j] - vFences[i])
        
        #largest common distance (common values)
        common = h_distances & v_distances
        
        if not common:
            return -1
        
        max_side = max(common)
        return (max_side * max_side) % MOD