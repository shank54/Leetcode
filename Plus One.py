class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]
        carry = 1
        i = len(digits)-1
        if digits[i]<9:
            digits[i] += carry
            return digits
        while i>=0:
            if carry+digits[i] > 9:
                digits[i] = 0
                carry = 1
            else:
                digits[i] += carry
                carry = 0
                return digits
            i -= 1
        return [1]+digits