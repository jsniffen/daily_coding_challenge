# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.e

import time

class Scheduler:
    def __init__(self, delay, func, *args, **kwargs):
        self.func = func
        self.delay = delay
        self.answer = None
        self.args = args
        self.kwargs = kwargs

        time.sleep(delay)
        self.answer = func(*args, **kwargs)

    def result(self):
        return self.answer

def add(x, y):
    return x + y

s = Scheduler(1, add, 10, 20)
print(s.result())
