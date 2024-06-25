class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        left = 0
        right = 1
        target = chars[left]
        point = 0
        cnt = 1
        if len(chars) == 1:
            return 1
        while right<=len(chars):
            if right == len(chars):
                chars[point] = target
                if cnt != 1:
                    cnt_len = len(str(cnt))
                    for i in range(cnt_len):
                        chars[point+i+1] = str(cnt)[i]
                    cnt = 1
                    point += cnt_len+1
                else:
                    point += 1
                break
            if chars[right] == target:
                cnt += 1
                right += 1
            else:
                chars[point] = target
                if cnt != 1:
                    cnt_len = len(str(cnt))
                    for i in range(cnt_len):
                        chars[point+i+1] = str(cnt)[i]
                    cnt = 1
                    point += cnt_len
                target = chars[right]
                point += 1
                left = right
                right += 1
        chars = chars[0:point]

        return len(chars)