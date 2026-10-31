class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ans = 0
        for symbol in tokens:
            
            if symbol == '*':
                s = stack.pop()
                f = stack.pop()
                stack.append(f*s)
                print(stack[-1])
            elif symbol == '/':
                s = stack.pop()
                
                f = stack.pop()
                stack.append(int(f/s))
                
            elif symbol == '+':
                s = stack.pop()
                f = stack.pop()
                stack.append(f+s)
                print(stack[-1])
            elif symbol == '-':
                s = stack.pop()
                f = stack.pop()
                stack.append(f-s)
            else:
                stack.append(int(symbol))
                
            
        return stack[0]




        '''
        stack = []
        ans = 0

        for num in arr:
            # for monotonic decreasing, just flip the > to <
            while stack and stack[-1] > num:
                # do logic
                stack.pop()
            stack.append(num)
            '''
        
        return ans