# 1344. Angle Between Hands of a Clock

# Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.
# Answers within 10-5 of the actual value will be accepted as correct.

# Example 1:
# Input: hour = 12, minutes = 30
# Output: 165

# Example 2:
# Input: hour = 3, minutes = 30
# Output: 75

# Example 3:
# Input: hour = 3, minutes = 15
# Output: 7.5

# Constraints:
# 1 <= hour <= 12
# 0 <= minutes <= 59

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        # angle between sections
        min_angle_per_min = 6
        hour_angle_per_hour = 30

        if hour == 12:
            hour = 0

        # from 0
        min_angle = minutes * min_angle_per_min

        # from 0 including the fractional part from the minutes
        hour_angle = (hour * hour_angle_per_hour) + (minutes * 0.5)

        diff = abs(hour_angle - min_angle)

        return min(diff, 360 - diff)
        