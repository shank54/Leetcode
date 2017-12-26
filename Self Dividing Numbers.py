class Solution(object):
    def selfDividingNumbers(self, left, right):
        output = []
        for i in range(left,right+1):
            count = 0
            for num in str(i):
                if int(num)!=0 and int(int(i))%int(num) ==0:
                    count += 1
                else:
                    break
            if count == len(str(i)):
                output.append(i)
        return output