## 2차원 배열을 회전시키는 메소드  

```python
def rotate_a_matrix_by_90_degrees(a):
	n = len(a)
	m = len(a[0])
	result = [[0]*n for _ in range(m)] #결과 리스트
	for i in range(n):
		for j in range(m):
			result[j][n-i-1] = a[i][j]
	return result
```
---
관련 문제 :  
프로그래머스 - [자물쇠와 열쇠](https://programmers.co.kr/learn/courses/30/lessons/60059)