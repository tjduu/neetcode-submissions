class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        countt = {}
        
        for i in range(len(s)):
            counts[s[i]] = 1 + counts.get(s[i],0)

        for j in range(len(t)):
            countt[t[j]] = 1 + countt.get(t[j],0)
        
        
        return countt == counts
        
        