class Solution:
    def isValid(self, s: str) -> bool:
        left = [ '(','{' ,'[']
        right = [')','}', ']']
        stack = []
        for char in s:
            if char in left:
                stack.append(char)

            if char in right:
                if len(stack) ==0: 
                    return False
                if left.index(stack.pop()) != right.index(char):
                    return False
        return len(stack) == 0


        