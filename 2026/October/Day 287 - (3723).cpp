// 3723. Maximize Sum of Squares of Digits
// Medium
// Topics
// premium lock icon
// Companies
// Hint
// You are given two positive integers num and sum.

// A positive integer n is good if it satisfies both of the following:

// The number of digits in n is exactly num.
// The sum of digits in n is exactly sum.
// The score of a good integer n is the sum of the squares of digits in n.

// Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.

 

// Example 1:

// Input: num = 2, sum = 3

// Output: "30"

// Explanation:

// There are 3 good integers: 12, 21, and 30.

// The score of 12 is 12 + 22 = 5.
// The score of 21 is 22 + 12 = 5.
// The score of 30 is 32 + 02 = 9.
// The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

// Example 2:

// Input: num = 2, sum = 17

// Output: "98"

// Explanation:

// There are 2 good integers: 89 and 98.

// The score of 89 is 82 + 92 = 145.
// The score of 98 is 92 + 82 = 145.
// The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is "98".

// Example 3:

// Input: num = 1, sum = 10

// Output: ""

// Explanation:

// There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is "".

 

// Constraints:

// 1 <= num <= 2 * 105
// 1 <= sum <= 2 * 106


/*
This was Chosen to be written as a C++ solution to help me prepare for my job interview.
*/
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        // Check if the sum is within valid bounds (min possible sum is 1 if num > 0, max is num * 9)
        if (sum < 1 || sum > num * 9) {
            return "";
        }
        
        string result = "";
        for (int i = 0; i < num; ++i) {
            // Find the maximum digit we can place at position i
            // leave enough sum for the remaining (num - 1 - i) digits (at most 9 each)
            int max_digit = min(9, sum);
            int min_needed = sum - (num - 1 - i) * 9;
            if (min_needed > 0) {
                max_digit = min(max_digit, max_digit); // keeping within bounds
            }
            
            // To maximize the score, we want the largest digit possible. 
            // Greedily take the largest valid digit for this position:
            int chosen = sum - (num - 1 - i) * 9;
            // ensure that the chosen digit is between 0-9
            chosen = max(0, chosen);
            chosen = min(9, chosen);
            // take the largest possible digit to get the largest possible score (where possible)
            int d = min(9, sum);
            // Ensure the rest can be formed:
            while (d >= 0 && sum - d > (num - 1 - i) * 9) {
                d--;
            }
            result += to_string(d);
            sum -= d;
        }
        
        return result;
    }
};




/*
This can also be done by:
*/
class Solution {
public:
    string maxSumOfSquares(int num, int sum) {
        // Base Case: it cant be made (too big or too small)
        if (sum < 1 || sum > 9 * num) {
            return "";
        }
        
        string res;
        res.reserve(num); // can hold atleast num without needing fragmentations -> improve efficiency
        
        // determine how many 9 can be used, and how many other numbers are left (the alrger numbers contribute exponentially to score)
        int n = sum / 9;
        int r = sum % 9;
        
        res.append(n, '9'); // add the 9 if possible
        num -= n;
        
        // handle remaining digists
        if (r) {
            res += '0' + r;
            --num;
        }
        
        // pad all other spaces with 0's ponce the 9's are added and the remainders are added to te right
        res.append(num, '0');
        
        return res;
    }
};