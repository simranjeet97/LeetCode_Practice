class Solution(object):
    def longestPalindrome(self, s):
        def expand(str, low, high):
            #Expand in Both directions Same as Window Sliding
            length = len(s)
            while low >= 0 and high < length and str[low] == str[high]:
                low = low - 1
                high = high + 1
            return str[low + 1:high]


        max_str = ""
        length = len(s)
        max_length = 0

        for i in range(length):

            # find the longest odd length palindrome with `str[i]` as a midpoint
            curr_str = expand(s, i, i)
            curr_length = len(curr_str)

            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str
            
            #Evem Length
            curr_str = expand(s, i, i + 1)
            curr_length = len(curr_str)

            if curr_length > max_length:
                max_length = curr_length
                max_str = curr_str

        return max_str
