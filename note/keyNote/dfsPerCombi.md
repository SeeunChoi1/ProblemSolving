## DFS로 구현하는 순열/조합

- 순열 Permutation   
nPr 순서 상관 있음   
```python
def permu(idx, n, pick, tmp):
    if len(tmp) == pick:
        picked_friends.append(tmp[:])
        return
    for i in range(idx, n):
        permu(i+1, n, pick, tmp+[i])
```

- 조합 Combination   
nCr 순서 상관 없음   
```python
def combi(idx, n, pick, tmp):
    if len(tmp) == pick:
        start_points.append(tmp[:])
        return
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = 1
            combi(i+1, n, pick, tmp+[i])
            visited[i] = 0
```
![img](/note/img/img1.png)

---
관련 문제 :  
프로그래머스 - [외벽 점검](https://programmers.co.kr/learn/courses/30/lessons/60062)