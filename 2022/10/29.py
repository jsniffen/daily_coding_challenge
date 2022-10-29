# Good morning! Here's your coding interview problem for today.
# 
# This problem was asked Microsoft.
# 
# Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
# 
# For example, given a file with the content 'Hello world', three read7() returns 'Hello w', 'orld' and then ''.

class File:
    def __init__(self, content):
        self.content = content

    def readN(self, n):
        data = self.content[:n]
        self.content = self.content[n:]
        return data

file = File("Hello world")

assert file.readN(7) == "Hello w"
assert file.readN(7) == "orld"
assert file.readN(7) == ""
