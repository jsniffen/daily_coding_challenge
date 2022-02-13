# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Airbnb.
# 
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# 
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# 
# Follow-up: Can you do this in O(N) time and constant space?

def largest_sum(nums):
    dp = [0] * len(nums)

    for i in range(len(nums)):
        if i <= 1:
            dp[i] = nums[i]
        elif i == 2:
            dp[i] = nums[i] + dp[i-2]
        else:
            dp[i] = nums[i] + max(dp[i-3], dp[i-2])

    return dp[len(nums)-1]

from collections import deque

def largest_sum_constant(nums):
    queue = deque([])

    longest = 0
    for i in range(len(nums)):
        if i <= 1:
            curr = nums[i]
        elif i == 2:
            curr = nums[i] + queue[0]
        else:
            p2 = queue.popleft()
            p1 = queue[0]
            curr = nums[i] + max(p1, p2)

        queue.append(curr)
        print(queue)
        longest = max(longest, curr)

    return longest

# assert largest_sum_constant([2, 4, 6, 2, 5]) == 13
# assert largest_sum_constant([5, 1, 1, 5]) == 10

# assert largest_sum([2, 4, 6, 2, 5]) == 13
# assert largest_sum([5, 1, 1, 5]) == 10
