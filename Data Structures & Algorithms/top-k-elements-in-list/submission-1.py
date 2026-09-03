class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1

        rank = []
        for num, cnt in count.items():
            rank.append([cnt,num])
        rank.sort()

        res = []

        while len(res) < k:
            res.append(rank.pop()[1])
        return res
        
            


