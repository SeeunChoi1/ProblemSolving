class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # append into dictionary
        dic = {}
        for log in logs:
            key = log.split()[0]
            dic[key] = log[len(key)+1:]
            
        # classify letter-logs and digit-logs
        letter_dic = {}
        digit_dic = {}
        for key, value in dic.items():
            print(value[0:1])
            if value[0:1].isdigit() : 
                digit_dic[key] = value
            else:
                letter_dic[key] = value
        
        #dictionary -> list
        letter_list = []
        digit_list = []
        [letter_list.append(k + ' '+ v) for k, v in letter_dic.items()]
        [digit_list.append(k + ' ' + v) for k, v in digit_dic.items()]
        
        #sort
        letter_list.sort()
        digit_list.sort()
    # 망함
    # 1. dictionary를 쓰기 시작하니 sort가 안됨. 메모리를 너무 많이 잡아먹음
    # 2. sort도 key값으로 하면 차라리 나을텐데 value값으로 sort를 해야해서 복잡해짐

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters, digits = [], []
        
        # classify list and digit
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        # sort by lambda x:(식별자, 후순위 식별자)
        letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        return letters + digits
        