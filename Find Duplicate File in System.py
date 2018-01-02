class Solution(object):
    def findDuplicate(self, paths):
        d = dict()
        for i in paths:
            dir = i.split(" ")
            resdir = dir[0]
            for txt in dir[1:]:
                fname = txt.split("(")
                filename = fname[0] # filename 1.txt
                contents = fname[1][:-1]
                d.setdefault(contents,[])
                if contents in d:
                    d[contents].append(resdir+"/"+filename)
        resultlist = []
        for i in d:
            if len(d[i])>1:
                resultlist.append(d[i])
        return resultlist