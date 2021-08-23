def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1

def romanToDecimal(str):
    res = 0
    i = 0
 
    while (i < len(str)):
 
        # Getting value of symbol s[i]
        s1 = value(str[i])
 
        if (i + 1 < len(str)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(str[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res


 #-----------------------------------------------------------------------------
class Solution:
    def romanToInt(self, s):
	    # use dictionary for value lookup
        dictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        last_value = 0
        sum_of_value = 0
		# look at values from reverse (smallest to biggest)
        for char in reversed(s):
            current_value = dictionary[char]
			# only need to subtract if the current value is less than previous value
			# do not update last_value so we keep the larger last value
            if last_value > current_value:
                sum_of_value -=current_value
            else:
                sum_of_value +=current_value
                last_value = current_value
                
        return sum_of_value

