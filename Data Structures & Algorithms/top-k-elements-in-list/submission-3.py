class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
    
        sorted_v = sorted(count.items(),key = lambda item : item[1])
        
        res = []
        while len(res) < k:            
            item = sorted_v.pop()      
            res.append(item[0]) 
        return res
