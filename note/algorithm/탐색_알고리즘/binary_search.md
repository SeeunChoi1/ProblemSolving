# 이진 탐색 (Binary Search)
- 이진탐색은 전제 조건이 데이터 정렬이다.
- 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며** 데이터를 탐색하는 방법
    - 찾으려는 데이터와 중간점(Middle) 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾음
    - 시작점, 끝점, 중간점이 필요함
- 시간 복잡도가 log 가 됨 (단계마다 2로 나누는 것과 동일하므로 연산 횟수는 logN에 비례한다고 할 수있다)

## 재귀로 구현
```python
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    # 중간 점의 값 보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

arr =[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
re = binary_search(arr, 4, 0, len(arr))
if re == None:
    print('결과가 존재하지 않습ㅈ니다.')
else:
    print(re)
```

## 반복문으로 구현
```python
def binary_search(arr, target, start, end):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None

arr =[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
re = binary_search(arr, 4, 0, len(arr))
print(re)
```

### 파이썬 이진 탐색 라이브러리
- bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
- bisect_right(a, x) :  정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

### 파라메트릭 서치 → 이진탐색을 이용하여 해결 가능
- 최적화 문제를 결정 문제(예 또는 아니오) 로 바꾸어 해결하는 기법입니다.
    - 예시 ) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
- 참고문제
    - [떡볶이 떡 만들기](https://github.com/SeeunChoi1/python-for-coding-test/blob/master/07/2.py)
    - [공유기 설치](https://github.com/SeeunChoi1/python-for-coding-test/blob/master/07/5.py) [/ 문제 출처: 백준](https://www.acmicpc.net/problem/2110)

- 데이터베이스는 내부적을 **트리 자료구조**를 이용하여 항상 데이터가 정렬 되어있다.
    - 참고자료 >> [트리](../dataStructure/tree.md)

---
참고
- 이것이 취업을 위한 코딩 테스트이다 (with Python) - 나동빈 저 
- [ssongplay/[Python] bisect 라이브러리](https://velog.io/@ssongplay/Python-bisect-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC)

[⬅️ 탐색](/note/algorithm/search.md)
[🏠 목록으로](/README.md)