class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortd = defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            sortd[ss].append(s)
    
        return list(sortd.values())

           
          
          
