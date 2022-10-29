# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Facebook.
# 
# Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.
# 
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.


def max_profit(prices):
    max_profit, mini = -float("inf"), float("inf")

    for n in prices:
        if n < mini:
            mini = n
        else:
            profit = n - mini
            if profit > max_profit:
                max_profit = profit

    return max_profit


assert max_profit([9, 11, 8, 5, 7, 10]) == 5
