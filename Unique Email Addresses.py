class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        d = dict()
        for email in emails:
            flag = 0
            temp = ""
            for j in email:
                if j=="@":
                    flag = 1
                if j=="+":
                    flag = 2
                if flag == 0:
                    if j!=".":
                        temp += j
                if flag == 1:
                    temp += j
            if temp not in d:
                d[temp] = 1
            else:
                d[temp] += 1
        return len(d)
        