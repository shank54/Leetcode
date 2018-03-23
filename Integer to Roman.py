class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        tmp = {1:"I",4:"IV",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        d1 = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        d2 = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        
        res = ""
        for i in range(len(d1)):
            while num>=d1[i]:
                num -= d1[i]
                res += d2[i]
        return res