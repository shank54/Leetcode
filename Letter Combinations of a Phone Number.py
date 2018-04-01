class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        tmp1 = [0,1,2,3,4,5,6,7,8,9]
        tmp2 = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        b = 1
        res = list(tmp2[int(digits[0])])
        for k in range(len(digits)-1):
            if digits[b] == "0" or digits[b] == "1":
                return []
            l1 = res
            #l1 = res, l2 = s[b+1]
            l2 = tmp2[int(digits[b])]
            tmp3 = []
            for i in range(len(l1)):
                for j in range(len(l2)):
                    x = l1
                    y = l2
                    tmp3.append(x[i]+y[j])
            res = tmp3
            b += 1
        return res