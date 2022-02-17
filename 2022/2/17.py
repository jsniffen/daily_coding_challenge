# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked by Amazon.
# 
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# 
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substring(string, k):
    start = end = maxstart = maxend = 0 
    chars = {}

    while end < len(string):
        char = string[end]

        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

            while len(chars) > k:
                start_char = string[start]
                chars[start_char] -= 1

                if chars[start_char] == 0:
                    del chars[start_char]

                start += 1

        end += 1
        if end - start > maxend - maxstart:
            maxstart, maxend = start, end

    return string[maxstart:maxend]

assert longest_substring("abcba", 2) == "bcb"
