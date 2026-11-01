class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0 for x in range(0, len(temperatures))]
        for i in range(0, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop = stack.pop()
                ans[pop] = i - pop
            stack.append(i)
        return ans
        #[30,38,30,36,35,40,28]
        #[30,38]