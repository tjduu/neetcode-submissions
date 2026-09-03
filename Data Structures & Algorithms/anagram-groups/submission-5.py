class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          dicts = defaultdict(list)
          
          for s in strs:
               sstring = "".join(sorted(s))
               dicts[sstring].append(s)
          
          return list(dicts.values())

          
          
