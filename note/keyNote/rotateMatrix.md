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