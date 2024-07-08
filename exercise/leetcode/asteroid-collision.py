from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            print(ans)
            if not ans:
                ans.append(a)
                continue
            if ans[-1] * a > 0: # 둘이 부호 같음
                ans.append(a)
            else:
                last = ans.pop()
                if last > 0:
                    if a + last == 0:
                        continue
                    next = a if abs(a) > abs(last) else last
                    ans.append(next)
                else:
                    ans.append(last)
                    ans.append(a)

            # 하나 넣을 때 마다
            # 기존 것과 충돌 나는지 확인
            if len(ans) > 1 and ans[-1] * ans[-2] < 0:
                # 방금 넣은 것이 아니라는 것
                if ans[-2] < 0:
                    continue
                just = ans.pop()
                bef = ans.pop()
                if just + bef == 0:
                    continue
                next = just if abs(just) > abs(bef) else bef
                ans.append(next)
        return ans