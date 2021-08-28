class Solution(object):
    def letterCombinations(self, digits):
        d={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
             "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        s = []
        if digits == "":
            return s
        
        for i in digits:
            s.append(d[i])
        return ["".join(x) for x in itertools.product(*s)]