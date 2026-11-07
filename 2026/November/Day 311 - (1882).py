# 1882. Process Tasks Using Servers

# You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.
# Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.
# At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.
# If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.
# A server that is assigned task j at second t will be free again at second t + tasks[j].
# Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.
# Return the array ans​​​​.

# Example 1:
# Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
# Output: [2,2,0,2,1,2]
# Explanation: Events in chronological order go as follows:
# - At second 0, task 0 is added and processed using server 2 until second 1.
# - At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
# - At second 2, task 2 is added and processed using server 0 until second 5.
# - At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
# - At second 4, task 4 is added and processed using server 1 until second 5.
# - At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.

# Example 2:
# Input: servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
# Output: [1,4,1,4,1,3,2]
# Explanation: Events in chronological order go as follows: 
# - At second 0, task 0 is added and processed using server 1 until second 2.
# - At second 1, task 1 is added and processed using server 4 until second 2.
# - At second 2, servers 1 and 4 become free. Task 2 is added and processed using server 1 until second 4. 
# - At second 3, task 3 is added and processed using server 4 until second 7.
# - At second 4, server 1 becomes free. Task 4 is added and processed using server 1 until second 9. 
# - At second 5, task 5 is added and processed using server 3 until second 7.
# - At second 6, task 6 is added and processed using server 2 until second 7.

# Constraints:
# servers.length == n
# tasks.length == m
# 1 <= n, m <= 2 * 105
# 1 <= servers[i], tasks[j] <= 2 * 105


class Solution(object):
    def assignTasks(self, servers, tasks):
        """
        :type servers: List[int]
        :type tasks: List[int]
        :rtype: List[int]
        """
        # master time loop iterating over the sum of tasks
        # loop throgh the tasks (the queue) and add them to the first free server if possible (if more than one free, assign based on index)
        #   update the ques following atempted implementation (jump to the next available server free point (store the minimum weight of a task across all servers (this is the jump)))

        # From an answering POV:
        # the first n elements are numbered as such, then following that, tract the smallest element for time jumps

        n = len(servers)
        m = len(tasks)
        
        # Heap of available servers: tuples of (weight, index)
        available = []
        for i in range(n):
            heapq.heappush(available, (servers[i], i))
            
        # Heap of unavailable servers: tuples of (free_time, weight, index)
        unavailable = []
        
        ans = []
        current_time = 0
        
        for j in range(m):
            # If current_time has fallen behind the task arrival time, jump ahead
            current_time = max(current_time, j)
            
            # If no servers are available, jump time to the exact moment the next server frees up
            if not available and unavailable[0][0] > current_time:
                current_time = unavailable[0][0]
                
            # Move any servers that have finished their tasks back to the available pool
            while unavailable and unavailable[0][0] <= current_time:
                free_time, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
                
            # Assign the current task to the best available server
            weight, index = heapq.heappop(available)
            ans.append(index)
            
            # Push the server into the unavailable heap with its new completion time
            task_duration = tasks[j]
            heapq.heappush(unavailable, (current_time + task_duration, weight, index))
            
        return ans

'''
Once again, i was not faithful to the idea of this coding challeng. While all throght processes were mine, 
the code itself is not and was generated by gemini.ai. Why you may ask...well today I couldnt be bothered. Sadly,
this is becoming more of a recuring them. Will all the additional coding around job interviews and work, im loosing
the will to do this for fun. Sadly, it was more about the process than the code this time; thats something i need to
change if i want to improve.

Similarly my language practice is suffering. I need to get back into reading and writing in Turkish aswell but im
in  a'can't be bothered' frame of mind.
'''