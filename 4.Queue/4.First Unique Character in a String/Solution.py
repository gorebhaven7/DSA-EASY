class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = []
        visited = []
        for e in s:
            if e not in l :
                if e not in visited:
                    l.append(e)
                visited.append(e)
            else:
                l.remove(e)
        
        if len(l) == 0:
            return -1
        else:
            return s.find(l.pop(0))