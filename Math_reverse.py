
def reverse(x):
        def boundery_check(reversed):
            upper = pow(2, 31) - 1
            lower = -pow(2, 31)
            print(lower)
            if reversed >= upper or reversed < lower:
                return 0
            else:
                return reversed

        # finding sige
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        # divid by 10 power
        dn = 1
        i = 1
        reversed = ""
        while (True):

            f = pow(10, i)
            res = x % f
            res = res / (pow(10, i - 1))
            dn = x // f
            reversed += str(int(res))
            x = x - (pow(10, i - 1) * res)
            if dn != 0:
                i += 1
            else:
                break
        number = int(reversed)
        print(number)
        print(number*sign)
        return (boundery_check(sign * number))



print(reverse(-2147483648))


