class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = {}
        for i ,num in enumerate(nums):
            A[num] = i
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in A and A[dif] !=i:
                return [i,A[dif]]



