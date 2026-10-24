# 2409. Count Days Spent Together

# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

# Example 1:
# Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
# Output: 3
# Explanation: Alice will be in Rome from August 15 to August 18. Bob will be in Rome from August 16 to August 19. They are both in Rome together on August 16th, 17th, and 18th, so the answer is 3.

# Example 2:
# Input: arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
# Output: 0
# Explanation: There is no day when Alice and Bob are in Rome together, so we return 0.

# Constraints:
# All dates are provided in the format "MM-DD".
# Alice and Bob's arrival dates are earlier than or equal to their leaving dates.
# The given dates are valid dates of a non-leap year.

class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        # Days in each month for a non-leap year
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def date_to_day_number(date_str):
            month = int(date_str[:2])
            day = int(date_str[3:])
            # Sum days of previous months + current day
            return sum(days_in_months[:month - 1]) + day

        # Convert all dates to day numbers of the year
        alice_arrive = date_to_day_number(arriveAlice)
        alice_leave = date_to_day_number(leaveAlice)
        bob_arrive = date_to_day_number(arriveBob)
        bob_leave = date_to_day_number(leaveBob)

        # Find the overlap interval
        overlap_start = max(alice_arrive, bob_arrive)
        overlap_end = min(alice_leave, bob_leave)

        # Calculate the total overlapping days
        if overlap_start <= overlap_end:
            return overlap_end - overlap_start + 1
        
        return 0