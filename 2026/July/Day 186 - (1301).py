# 1301. Number of Paths with Max Score

# You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.
# You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.
# Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
# In case there is no path, return [0, 0].

# Example 1:
# Input: board = ["E23","2X2","12S"]
# Output: [7,1]

# Example 2:
# Input: board = ["E12","1X1","21S"]
# Output: [4,2]

# Example 3:
# Input: board = ["E11","XXX","11S"]
# Output: [0,0]

# Constraints:
# 2 <= board.length == board[i].length <= 100

class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        n = len(board)
        MOD = 10**9 + 7
        
        # dp[r][c] will store [max_score, path_count]
        # Initialise with [-1, 0] to represent unvisited/unreachable cells (those not yet visited or not in the solution)
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        
        # Base case: Bottom-right corner 'S'
        dp[n-1][n-1] = [0, 1]
        
        # Iterate backwards from the bottom-right to the top-left
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                # Skip obstacles and the starting point (since it's already initialised)
                if board[r][c] == 'X' or (r == n - 1 and c == n - 1):
                    continue
                
                max_score = -1
                total_paths = 0
                
                # Check the 3 possible directions we could have come from:
                # Down, Right, and Down-Right Diagonal
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    
                    # If the neighbour is within bounds and reachable
                    if nr < n and nc < n and dp[nr][nc][0] != -1:
                        neighbor_score, neighbor_paths = dp[nr][nc]
                        
                        if neighbor_score > max_score:
                            max_score = neighbor_score
                            total_paths = neighbor_paths
                        elif neighbor_score == max_score:
                            total_paths = (total_paths + neighbor_paths) % MOD
                
                # If we found at least one valid path to this cell
                if max_score != -1:
                    # 'E' counts as 0, otherwise take the integer value of the cell
                    cell_value = 0 if board[r][c] == 'E' else int(board[r][c])
                    dp[r][c] = [max_score + cell_value, total_paths]
        
        # Extract the final result from the top-left cell 'E'
        final_score, final_paths = dp[0][0]
        
        # If 'E' is unreachable, return [0, 0]
        if final_score == -1:
            return [0, 0]
            
        return [final_score, final_paths]
    
    '''
    For ever cell which is a neighbour of the currrent leaf cells (those which are next in line form spreading
    out from the Bottom-Right), determine the score from each of the cells which can feed into it (looking at all 3).
    From here, continue up through alle the neighbours (tracking the length and number of ways of that value forom the route)
    Given then priority was given to those leaves with the greatest score (as these will result in a greater ending score).
    Once at the top, you will have all counts of the maximum score and number of ways to make it
    '''