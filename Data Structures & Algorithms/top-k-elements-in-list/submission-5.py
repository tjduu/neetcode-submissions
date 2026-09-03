class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        A = {}
        for num in nums:
            A[num] = A.get(num,0) + 1
        sorted_keys = sorted(A, key=A.get, reverse=True)

        
        return sorted_keys[:k]
        
