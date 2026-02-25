# 2977. Minimum Cost to Convert String 2

# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters.
# You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents 
# the cost of converting the string original[i] to the string changed[i].

# You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a 
# cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to 
# do any number of operations, but any pair of operations must satisfy either of these two conditions:

# The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the 
# indices picked in both operations are disjoint.
# The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the 
# indices picked in both operations are identical.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is 
# impossible to convert source to target, return -1.
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].


# Example 1:
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"],
# cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert "abcd" to "acbe", do the following operations:
# - Change substring source[1..1] from "b" to "c" at a cost of 5.
# - Change substring source[2..2] from "c" to "e" at a cost of 1.
# - Change substring source[2..2] from "e" to "b" at a cost of 2.
# - Change substring source[3..3] from "d" to "e" at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28. 
# It can be shown that this is the minimum possible cost.

# Example 2:
# Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"],
# cost = [1,3,5]
# Output: 9
# Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
# - Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
# - Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] 
# are disjoint with indices picked in the first operation.
# - Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] 
# are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
# The total cost incurred is 1 + 3 + 5 = 9.
# It can be shown that this is the minimum possible cost.

# Example 3:
# Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"],
# cost = [100,1578]
# Output: -1
# Explanation: It is impossible to convert "abcdefgh" to "addddddd".
# If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select 
# substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
# If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select 
# substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
 

# Constraints:
# 1 <= source.length == target.length <= 1000
# source, target consist only of lowercase English characters.
# 1 <= cost.length == original.length == changed.length <= 100
# 1 <= original[i].length == changed[i].length <= source.length
# original[i], changed[i] consist only of lowercase English characters.
# original[i] != changed[i]
# 1 <= cost[i] <= 106



#My first attempt too inspiration form my code from yesterday in teh Minimum COst to Convert String 1,
#with the only changes being that the transitions are now between substrings rather than single characters
#this approach did not work:
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        #follow thge same operations as Minimum Cost to Convert String 1
        #but apply it over larger stirng alphabet than single character alphabets

        all_substrings = set(original) | set(changed)
        substr_to_idx = {substr: i for i, substr in enumerate(sorted(all_substrings))}
        n = len(substr_to_idx)        
        
        # Initialize cost matrix (n x n, where n is number of unique chars)
        INF = float('inf')
        dist = [[INF] * n for _ in range(n)]
        
        # Cost to transform a letter to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Add direct transformation costs
        for i in range(len(original)):
            x = substr_to_idx[original[i]]
            y = substr_to_idx[changed[i]]
            dist[x][y] = min(dist[x][y], cost[i])  # Take minimum if duplicate
        
        # Step 2: Floyd-Warshall - find minimum costs for all pairs of substrings
        for k in range(n):  # intermediate vertex
            for i in range(n):  # source
                for j in range(n):  # destination
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


        # Step 3: Dynamic Programming with substring matching
        m = len(source)
        dp = [INF] * (m + 1)
        dp[0] = 0
        
        for i in range(1, m + 1):
            #Option 1: Characters already match, no cost
            if source[i - 1] == target[i - 1]:
                dp[i] = min(dp[i], dp[i - 1])
            
            #Option 2: Use a substring transformation
            for j in range(i):
                source_substr = source[j:i]
                target_substr = target[j:i]
                
                #check if this exact substring transformation exists
                if source_substr in substr_to_idx and target_substr in substr_to_idx:
                    x = substr_to_idx[source_substr]
                    y = substr_to_idx[target_substr]
                    
                    if dist[x][y] != INF:
                        dp[i] = min(dp[i], dp[j] + dist[x][y])
        
        #Return result
        return dp[m] if dp[m] != INF else -1   



#I could not get it to work. I was lonst and had no idea despite follwing the HINTS provided in the problem description
# so I had to resort to using the code provided as an example solution, with some slight adaptations
# comments were added by Claud to explain the code more clearly and help me understrrand what it does and why it works

# Constants for infinity values
INF = 10**18        # Large infinity for DP array
INF_INT = 10**9     # Smaller infinity for distance matrix (prevents overflow)

class Solution:
    def minimumCost(
        self,
        source,
        target,
        original,
        changed,
        cost,
    ):
        n = len(source)  # Length of source and target strings
        m = len(original)  # Number of transformation rules
        
        # Trie data structures (array-based for efficiency)
        child = [[-1] * 26]  # child[node][char] = next_node, -1 if no edge
        tid = [-1]           # tid[node] = transformation ID, -1 if not a complete substring
        idx = [-1]           # Counter for assigning unique IDs to substrings (list for mutability)
        
        def new_node():
            """Create a new Trie node and return its index"""
            child.append([-1] * 26)
            tid.append(-1)
            return len(child) - 1
        
        def add(word):
            """
            Add a word to the Trie and return its unique transformation ID.
            If the word already exists, return its existing ID.
            """
            node = 0  # Start at root
            for ch in word:
                c = ord(ch) - 97  # Convert 'a'-'z' to 0-25
                nxt = child[node][c]
                if nxt == -1:  # Edge doesn't exist
                    nxt = new_node()
                    child[node][c] = nxt
                node = nxt
            
            # Mark this node as a complete substring
            if tid[node] == -1:
                idx[0] += 1
                tid[node] = idx[0]
            return tid[node]
        
        # Step 1: Build graph edges from transformation rules
        edges = []
        for i in range(m):
            x = add(original[i])  # Get ID for source substring
            y = add(changed[i])   # Get ID for target substring
            edges.append((x, y, cost[i]))
        
        P = idx[0] + 1  # Total number of unique substrings
        if P == 0:
            # No transformations available
            return 0 if source == target else -1
        
        # Step 2: Initialize distance matrix for substring transformations
        dist = [[INF_INT] * P for _ in range(P)]
        for i in range(P):
            dist[i][i] = 0  # Cost to transform substring to itself is 0
        
        # Add direct transformation costs
        for x, y, w in edges:
            if w < dist[x][y]:
                dist[x][y] = w
        
        # Step 3: Floyd-Warshall algorithm to find shortest paths between all substring pairs
        for k in range(P):  # Intermediate vertex
            dk = dist[k]
            for i in range(P):  # Source
                di = dist[i]
                dik = di[k]
                if dik == INF_INT:
                    continue  # Skip if no path from i to k
                base = dik
                for j in range(P):  # Destination
                    nd = base + dk[j]  # Path through k
                    if nd < di[j]:
                        di[j] = nd
        
        # Step 4: Dynamic Programming to find minimum cost transformation
        dp = [INF] * (n + 1)  # dp[i] = min cost to transform source[0:i] to target[0:i]
        dp[0] = 0  # Base case: empty strings match with 0 cost
        
        # Precompute character indices for faster access
        s_arr = [ord(c) - 97 for c in source]
        t_arr = [ord(c) - 97 for c in target]
        
        for j in range(n):
            if dp[j] >= INF:
                continue  # Skip impossible states
            
            base = dp[j]
            
            # Option 1: Characters already match (no transformation needed)
            if source[j] == target[j] and base < dp[j + 1]:
                dp[j + 1] = base
            
            # Option 2: Try substring transformations starting at position j
            u = 0  # Trie node for source substring
            v = 0  # Trie node for target substring
            
            for i in range(j, n):
                # Traverse both Tries simultaneously
                u = child[u][s_arr[i]]
                v = child[v][t_arr[i]]
                
                # If either path doesn't exist in Trie, stop searching
                if u == -1 or v == -1:
                    break
                
                uid = tid[u]  # Transformation ID for source substring
                vid = tid[v]  # Transformation ID for target substring
                
                # If both form valid substrings in our vocabulary
                if uid != -1 and vid != -1:
                    w = dist[uid][vid]  # Cost to transform source substring to target substring
                    if w != INF_INT:
                        ni = i + 1  # Next position after transformation
                        cand = base + w  # Total cost if we use this transformation
                        if cand < dp[ni]:
                            dp[ni] = cand
        
        # Return final answer
        ans = dp[n]
        return -1 if ans >= INF else ans