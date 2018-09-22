class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        flag =0
        if numerator<0 or denominator<0:
            flag = 1
        if numerator<0 and denominator<0:
            flag = 0
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator>2**31:
            numerator = 2147483647
        if denominator>2**31:
            denominator = 2147483647
        if numerator%denominator == 0:
            if flag:
                return "-"+str(numerator/denominator)
            return str(numerator/denominator)
        else:
            ans = str(numerator/denominator)+"."
            rem = (numerator%denominator)
            #res = str(float(rem/denominator))
            d = dict()
            while rem != 0:
                if rem in d:
                    t1 = d[rem]
                    ans = ans[:t1]+"("+ans[t1:]+")"
                    if flag:
                        return "-"+ans
                    return ans
                d[rem] = len(ans)
                rem *= 10
                ans += str(rem/denominator)
                rem = rem%denominator
            if flag:
                return "-"+ans
            return ans
                
            