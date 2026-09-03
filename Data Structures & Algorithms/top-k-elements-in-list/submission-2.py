class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        array = []
        for v,count in count.items():
            array.append([count,v])
        array.sort()

        res = []
        while k > len(res): 
            res.append(array.pop()[1])
        return res
        


