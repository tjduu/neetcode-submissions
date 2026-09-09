class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = [0] * len(temperatures)
        stack = []

        for i ,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stacki, stackt = stack.pop()
                days = i - stacki
                ls[stacki] = days
            stack.append([i,temp])
        return ls

