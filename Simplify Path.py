class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stk = []
        for i in path.split("/"):
            if i:
                if i=="..":
                    if stk:
                        stk.pop()
                elif i!=".":
                    stk.append(i)
        return "/"+"/".join(stk)