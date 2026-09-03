class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
          anagram_map = {}
          for text in strs:
          
               sorted_text = "".join(sorted(text))
               
               # 2. If we haven't seen this sorted key yet, initialize an empty list
               if sorted_text not in anagram_map:
                    anagram_map[sorted_text] = []
               
               # 3. Append the ORIGINAL word to this sorted key's group
               anagram_map[sorted_text].append(text)
               
          # 4. Return just the grouped lists
          return list(anagram_map.values())
