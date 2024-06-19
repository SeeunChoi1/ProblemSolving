class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        s_list = list(s)
        queue = []
        # for elem in s:
        #     if elem.lower() in vowels:
        #         queue.append(elem)
        # for i in range(len(s_list)):
        #     if s_list[i].lower() in vowels:
        #         s_list[i] = queue[-1]
        #         queue.pop(-1)
        # return "".join(s_list)

        for elem in s:
            if elem.lower() in vowels:
                queue.append(elem)
        pointer = len(queue) - 1
        for i in range(len(s_list)):
            if s_list[i].lower() in vowels:
                s_list[i] = queue[pointer]
                pointer -= 1
        return "".join(s_list)


