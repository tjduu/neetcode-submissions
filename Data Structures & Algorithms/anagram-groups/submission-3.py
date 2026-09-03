class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          dicts = defaultdict(list)
          for text in strs:
               key = "".join(sorted(text))
               dicts[key].append(text)
          return list(dicts.values())