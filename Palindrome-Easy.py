class Solution(object):
    def isPalindrome(self, x):
        if x > 0:
            return x == int(str(x)[::-1])
        if x < 0:
            a = str(x)[::-1]
            return x == a
        if x == 0:
            return x == int(str(x))