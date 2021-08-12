class Solution(object):
    def myAtoi(self, s):
        SPACE_CHARACTERS = " "
        SIGNAL_CHARACTERS = "+-"
        DIGIT_CHARACTERS = "0123456789"
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        sign = None
        spaces_ended = False
        digits = []
        str = s

        for char in str:
            if char in SPACE_CHARACTERS and not spaces_ended:
                continue
            else:
                spaces_ended = True
            if char in SIGNAL_CHARACTERS and not sign:
                sign = 1 if char == "+" else -1

            elif char in DIGIT_CHARACTERS:
                sign = 1 if not sign else sign
                digits.append(char)
            else:
                break
        
        total = 0
        sign = 1 if not sign else sign

        for i in range(0, len(digits)):
            total += DIGIT_CHARACTERS.index(digits[i]) * 10**(len(digits)-i-1)
        total*= sign
        
        if total < INT_MIN:
            return INT_MIN
        elif total > INT_MAX:
            return INT_MAX
        else:
            return total