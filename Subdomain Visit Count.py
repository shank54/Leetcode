class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        d = dict()
        for i in cpdomains:
            num,domain = i.split()
            sub = domain.split(".")
            if str(domain) not in d:
                d[str(domain)] = int(num)
            else:
                d[str(domain)] += int(num)
            j = 0
            while j<len(domain):
                if domain[j] == ".":
                    if str(domain[j+1:]) not in d:
                        d[str(domain[j+1:])] = int(num)
                    else:
                        d[str(domain[j+1:])] += int(num)
                j += 1
        res = []
        s = ""
        for i in d:
            s = str(d[i])+" "+i
            res.append(s)
        return res