def intToRoman(num):
    ntr = {1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
    placeval = 1
    res = ''
    while(num > 0):
        d = num % 10
        print("A",d)
        if d == 4 or d == 9:
            res = ntr[placeval] + ntr[(d+1)*placeval] + res
            print("45",res)
        elif d != 0:
            if d >= 5:
                res = ntr[5*placeval] + (d-5)*ntr[placeval] + res
                print("5",res)
            else:
                res = d*ntr[placeval] + res
                print("es5",res)
        placeval *= 10
        num //= 10
    return res
