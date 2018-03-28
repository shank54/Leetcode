class Solution(object):
    def originalDigits(self, s):
        
        res = [0]*10
        for i in s:
            if i=="z":
                res[0] += 1
            if i=="w":
                res[2] += 1
            if i=="u":
                res[4] += 1
            if i=="x":
                res[6] += 1
            if i=="g":
                res[8] += 1
            if i=="i":
                res[9] += 1 # i=5,6,8
            if i=="s":
                res[7] += 1 # s=6
            if i=="f":
                res[5] += 1 # f=4
            if i=="h":
                res[3] += 1 # h=8
            if i=="o":
                res[1] += 1 # o=0,2,4
        
        res[7] -= res[6]
        res[5] -= res[4]
        res[3] -= res[8]
        res[9] = res[9]-res[8]-res[6]-res[5]
        res[1] = res[1]-res[0]-res[2]-res[4]
        
        ans = ""
        for i in range(len(res)):
            ans += str(i)*res[i]
        
        return ans
        