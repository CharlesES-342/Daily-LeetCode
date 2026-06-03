# 3635. Earliest Finish Time for Land and Water Rides II

# You are given two categories of theme park attractions: land rides and water rides.
# Land rides
# landStartTime[i] – the earliest time the ith land ride can be boarded.
# landDuration[i] – how long the ith land ride lasts.
# Water rides
# waterStartTime[j] – the earliest time the jth water ride can be boarded.
# waterDuration[j] – how long the jth water ride lasts.
# A tourist must experience exactly one ride from each category, in either order.
# A ride may be started at its opening time or any later moment.
# If a ride is started at time t, it finishes at time t + duration.
# Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
# Return the earliest possible time at which the tourist can finish both rides.

# Example 1:
# Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]
# Output: 9
# Explanation:​​​​​​​
# Plan A (land ride 0 → water ride 0):
# Start land ride 0 at time landStartTime[0] = 2. Finish at 2 + landDuration[0] = 6.
# Water ride 0 opens at time waterStartTime[0] = 6. Start immediately at 6, finish at 6 + waterDuration[0] = 9.
# Plan B (water ride 0 → land ride 1):
# Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
# Land ride 1 opens at landStartTime[1] = 8. Start at time 9, finish at 9 + landDuration[1] = 10.
# Plan C (land ride 1 → water ride 0):
# Start land ride 1 at time landStartTime[1] = 8. Finish at 8 + landDuration[1] = 9.
# Water ride 0 opened at waterStartTime[0] = 6. Start at time 9, finish at 9 + waterDuration[0] = 12.
# Plan D (water ride 0 → land ride 0):
# Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
# Land ride 0 opened at landStartTime[0] = 2. Start at time 9, finish at 9 + landDuration[0] = 13.
# Plan A gives the earliest finish time of 9.

# Example 2:
# Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]
# Output: 14
# Explanation:​​​​​​​
# Plan A (water ride 0 → land ride 0):
# Start water ride 0 at time waterStartTime[0] = 1. Finish at 1 + waterDuration[0] = 11.
# Land ride 0 opened at landStartTime[0] = 5. Start immediately at 11 and finish at 11 + landDuration[0] = 14.
# Plan B (land ride 0 → water ride 0):
# Start land ride 0 at time landStartTime[0] = 5. Finish at 5 + landDuration[0] = 8.
# Water ride 0 opened at waterStartTime[0] = 1. Start immediately at 8 and finish at 8 + waterDuration[0] = 18.
# Plan A provides the earliest finish time of 14.​​​​​​​

# Constraints:
# 1 <= n, m <= 5 * 104
# landStartTime.length == landDuration.length == n
# waterStartTime.length == waterDuration.length == m
# 1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 105

'''
Initial Approach: made use of a binary search on a sorted [event, duration] pair, this was too slow
'''

'''
Next Approach: sort again sing finish times aswell, iterate thouh finding the best solution
This still took too long
'''
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # Create objects with start, duration, and their natural finish time
        land = sorted([(s, d, s + d) for s, d in zip(landStartTime, landDuration)], key=lambda x: x[2])
        water = sorted([(s, d, s + d) for s, d in zip(waterStartTime, waterDuration)], key=lambda x: x[2])

        ans = float('inf')

        # We really only need to check the activities that finish earliest
        # and a few candidates that start near the gap.
        # But to be 100% safe and efficient, let's look at the top candidates.
        
        for land_start, land_duration, land_finish in land:
            for water_start, water_duration, water_finish in water:
                # Land -> Water
                finish1 = max(land_finish, water_start) + water_duration
                # Water -> Land
                finish2 = max(water_finish, land_start) + land_duration
                
                res = min(finish1, finish2)
                if res < ans:
                    ans = res
                else:
                    # Optimisation: if the combo will be longer off of the initial event selection, skip (all solutions will be longer from here to the end as the events are ordered)
                    if water_start >= land_finish and (water_start + water_duration) >= ans:
                        break
        
        return ans
    
'''
Final Approach: using the hints
'''
class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        """
        :type landStartTime: List[int]
        :type landDuration: List[int]
        :type waterStartTime: List[int]
        :type waterDuration: List[int]
        :rtype: int
        """
        # Package and sort by start time
        land = sorted(zip(landStartTime, landDuration))
        water = sorted(zip(waterStartTime, waterDuration))
        
        def solve(listA, listB):
            n, m = len(listA), len(listB)
            # b_starts[j] = start time of j-th activity in listB
            b_starts = [x[0] for x in listB]
            
            # Prefix Min of Durations: min duration of all activities from 0 to j
            pref_min_dur = [0] * m
            curr_min_dur = float('inf')
            for j in range(m):
                curr_min_dur = min(curr_min_dur, listB[j][1])
                pref_min_dur[j] = curr_min_dur
                
            # Suffix Min of Finish Times: min (s+d) of all activities from j to m-1
            suff_min_finish = [0] * m
            curr_min_finish = float('inf')
            for j in range(m - 1, -1, -1):
                curr_min_finish = min(curr_min_finish, listB[j][0] + listB[j][1])
                suff_min_finish[j] = curr_min_finish
            
            best_for_order = float('inf')
            for s1, d1 in listA:
                f1 = s1 + d1
                # Find split point: where listB starts > f1
                idx = bisect.bisect_right(b_starts, f1)
                
                # Option A: Water activity starts before/at Land finishes
                # Result = f1 + min_duration of those activities
                if idx > 0:
                    best_for_order = min(best_for_order, f1 + pref_min_dur[idx-1])
                
                # Option B: Water activity starts after Land finishes
                # Result = min natural finish time of those activities
                if idx < m:
                    best_for_order = min(best_for_order, suff_min_finish[idx])
                    
            return best_for_order

        # Try both sequences: Land -> Water and Water -> Land
        res1 = solve(land, water)
        res2 = solve(water, land)
        
        return min(res1, res2)
    
    '''
    Generated by Gemini.ai
    How it works:
    By using the Prefix Min Duration, you are essentially saying: "If I have to wait for any of
    these $j$ activities anyway, I might as well pick the one that ends the fastest."

    By using the Suffix Min Finish, you are saying: "Since all these activities start after I'm
    ready, the gap doesn't matter; I just want to know which one gets me home earliest based on
    its own schedule."
    '''