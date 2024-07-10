class Solution:
    def decodeString(self, s: str) -> str:
        lst = list(s)
        ans = []
        stack = []
        for elem in lst:
            print(stack)
            if elem.isdigit():
                # print('number', elem)
                stack.append(elem)
            elif elem.isalpha():
                # print('char', elem)
                stack.append(elem)
            elif elem == '[':
                print('start')
            elif elem == ']':
                print('end')
                new = []
                while stack:
                    next = stack.pop()
                    new.append(next)
                    if next.isnumeric():
                        break
                print('pop end', new)
                num = new[-1]
                char = new[:len(new):-1]
                print(num, char)
