# 3700. Number of ZigZag Arrays II

# You are given three integers n, l, and r.
# A ZigZag array of length n is defined as follows:
# Each element lies in the range [l, r].
# No two adjacent elements are equal.
# No three consecutive elements form a strictly increasing or strictly decreasing sequence.
# Return the total number of valid ZigZag arrays.
# Since the answer may be large, return it modulo 109 + 7.
# A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).
# A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

# Example 1:
# Input: n = 3, l = 4, r = 5
# Output: 2
# Explanation:
# There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:
# [4, 5, 4]
# [5, 4, 5]

# Example 2:
# Input: n = 3, l = 1, r = 3
# Output: 10
# Explanation:
# ​​​​​​​There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:
# [1, 2, 1], [1, 3, 1], [1, 3, 2]
# [2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
# [3, 1, 2], [3, 1, 3], [3, 2, 3]
# All arrays meet the ZigZag conditions.

# Constraints:
# 3 <= n <= 109
# 1 <= l < r <= 75​​​​​​​

class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1
        size = 2 * m
        
        # --- Initialisation ---
        # State vector V combines [dp0, dp1] 
        # For length 1, every element has exactly 1 valid configuration.
        V = [1] * size
        
        # --- Construct the State Transition Matrix U ---
        # U has a block anti-diagonal structure: [[O, A], [B, O]]
        U = [[0] * size for _ in range(size)]
        for i in range(m):
            for j in range(m):
                if i < j:
                    U[i][m + j] = 1  # Matrix A (top-right block)
                if i > j:
                    U[m + i][j] = 1  # Matrix B (bottom-left block)
                    
        # --- Highly Optimised Matrix Multiplication Helpers ---
        def vec_mat_mul(v, M):
            """Multiplies a 1 x size vector by a size x size matrix."""
            res = [0] * size
            for i in range(size):
                vi = v[i]
                if vi == 0:
                    continue
                Mi = M[i]
                for j in range(size):
                    res[j] = (res[j] + vi * Mi[j]) % MOD
            return res

        def mat_mat_mul(M1, M2):
            """Multiplies a size x size matrix by another size x size matrix."""
            res = [[0] * size for _ in range(size)]
            for i in range(size):
                m1_i = M1[i]
                res_i = res[i]
                for k in range(size):
                    val = m1_i[k]
                    if val == 0:
                        continue
                    m2_k = M2[k]
                    for j in range(size):
                        res_i[j] = (res_i[j] + val * m2_k[j]) % MOD
            return res

        # --- Fast Matrix Exponentiation Loop ---
        exp = n - 1
        base = U
        res_v = V
        
        while exp > 0:
            if exp & 1:
                # Accumulate transitions directly onto the vector 
                # to save costly matrix-matrix multiplication steps
                res_v = vec_mat_mul(res_v, base)
            base = mat_mat_mul(base, base)
            exp >>= 1
            
        # Total valid sequences is the sum of all elements in the final combined state vector
        return sum(res_v) % MOD