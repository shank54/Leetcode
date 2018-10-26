class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        i = 0
        d = dict()
        res = 0
        for j in range(len(tree)):
            if tree[j] not in d:
                d[tree[j]] = 1
            else:
                d[tree[j]] += 1
            while len(d)>2:
                if d[tree[i]] == 1:
                    del d[tree[i]]
                else:
                    d[tree[i]] -= 1
                i += 1
            ans = 0
            for k in d:
                ans += d[k]
            res = max(res,ans)
        return res