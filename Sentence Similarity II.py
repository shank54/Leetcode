class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        graph = dict()
        for i in pairs:
            a,b = i
            if a in graph:
                graph[a].append(b)
            if b in graph:
                graph[b].append(a)
            if a not in graph:
                graph[a] = [b]
            if b not in graph:
                graph[b] = [a]
        
        for i in range(len(words1)):
            vis = []
            q = []
            vis.append(words1[i])
            q.append(words1[i])
            while q:
                tmp = q.pop(0)
                if tmp in graph:
                    for w in graph[tmp]:
                        if w not in vis:
                            vis.append(w)
                            q.append(w)
            if words2[i] not in vis:
                if words2[i] != words1[i]:
                    return False
        return True
            