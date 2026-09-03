class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = len(temperatures) * [0]
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stacki = stack.pop()
                ls[stacki] = i - stacki
            stack.append([temp,i])
        return ls

