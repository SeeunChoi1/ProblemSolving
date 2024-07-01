class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        # 서로 swap - 하나씩 -> 순서를 맘대로 해도 됨 -> 몇번이 걸리던 바꾸면 되니까
        # => 같은 종류의 알파벳이 같은 갯수로 잇으면 true임
        # 서로 swap - 해당 알파벳 전부
        # => 다른 종류여도 갯수 쌍만 맞으면 됨

        if len(word1) != len(word2):
            return False
        dict1 = {}
        dict2 = {}
        for w1 in word1:
            dict1[w1] = dict1[w1] + 1 if dict1.get(w1) else 1
        for w2 in word2:
            dict2[w2] = dict2[w2] + 1 if dict2.get(w2) else 1

        keys1 = sorted([i[0] for i in dict1.items()])
        keys2 = sorted([j[0] for j in dict2.items()])
        if len(keys1) != len(keys2):
            return False

        list1 = sorted([i[1] for i in dict1.items()])
        list2 = sorted([j[1] for j in dict2.items()])

        for idx in range(len(keys1)):
            if keys1[idx] != keys2[idx]:
                return False

        for idx in range(len(list1)):
            if list1[idx] != list2[idx]:
                return False
        return True
