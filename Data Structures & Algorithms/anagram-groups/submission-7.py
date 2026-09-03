class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            key[ss].append(s)
        
        return list(key.values())

           
          
          
