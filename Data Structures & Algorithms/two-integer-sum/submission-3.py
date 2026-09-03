class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       A = {}
       for i ,n in enumerate(nums):
            A[n] = i
       for i, n in enumerate(nums):
            diff = target - n
            if diff in A and A[diff]!=i:
                return [i,A[diff]]
        
            