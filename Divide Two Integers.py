class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag = 0
        if dividend<0 or divisor<0:
            flag = 1
        if dividend<0 and divisor<0:
            flag = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend>=divisor:
            temp = divisor
            count = 1
            while dividend>=temp<<1:
                temp *= 2
                count *= 2
            dividend -= temp
            res += count
        if flag:
            return max(res*(-1), -2147483648)
        return min(res, 2147483647)