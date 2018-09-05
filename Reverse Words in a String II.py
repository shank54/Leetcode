class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        i = 0
        j = len(str)-1
        while i<j:
            str[i],str[j] = str[j],str[i]
            i += 1
            j -= 1
        i = 0
        j = 0
        k = 0
        while j<len(str):
            if str[j] == " ":
                while i<k:
                    str[i],str[k] = str[k],str[i]
                    i += 1
                    k -= 1
                j += 1
                i = j                
            else:
                k = j
                j += 1
        while i<k:
            str[i],str[k] = str[k],str[i]
            i += 1
            k -= 1
        