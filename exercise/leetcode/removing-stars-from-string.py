class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for elem in s:
            if elem == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(elem)
        return "".join(stack)
