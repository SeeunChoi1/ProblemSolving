# 탐색
검색의 다른 명칭이 탐색  
검색 엔진에는 엔진이라는 이름이 붙어 있는데, 이를 엄밀하게 말하면 원하는 정보를 사람을 대신하여 찾아 주는 데이터 탐색 프로그램  
➡️ 이 데이터 탐색 프로그램에서 사용하고 있는 알고리즘이 바로 탐색 알고리즘   

> 탐색에서 빠르다는 것은 데이터가 많고 원하는 데이터가 배열의 끝 부분에 저장되어 있는 경우를 말하는 것  
>

## 선형 탐색 (Linear Search)
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
- 주로 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용함
- 시간복잡도는 배열의 크기에 따라 시간이 늘어나므로 O(n)으로 볼 수 있음
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
```
- 데이터 수가 많아지면 찾아내는 시간이 많이 소요되어 효율이 안좋아짐

## 이진 탐색 (Binary Search)
- 이진탐색은 전제 조건이 데이터 정렬이다.
- 정렬되어 있는 리스트에서 **탐색 범위를 절반씩 좁혀가며** 데이터를 탐색하는 방법
    - 찾으려는 데이터와 중간점(Middle) 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾음
    - 시작점, 끝점, 중간점이 필요함
- 시간 복잡도가 log 가 됨 (단계마다 2로 나누는 것과 동일하므로 연산 횟수는 logN에 비례한다고 할 수있다)

### 재귀로 구현
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

### 반복문으로 구현
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

## 해시 탐색법 (Hash Search)
> 해시 : 잘게 썬다, 잘게 자른다  
> 원래의 숫자를 모양이 변할 정도로 가공하여, 전혀 댜른 값을 생성한다.

- 데이터의 내용과 저장한 곳의 요소를 미리 연계해 둠으로써 극히 짧은 시간 안에 탐색할 수 있도록 고안된 알고리즘
    - 데이터를 데이터와 같은 첨자의 요소에 넣어 두면 한 번에 찾을 수 있지 않을까?
- 시간 복잡도는 O(1)로 나타낼 수 있음
    - 다만, 해시 충돌이 일어날 경우 O(n)
    - 해시 충돌로 인해 모든 bucket의 value들을 찾아봐야 하는 경우도 있기 때문
- 해시 탐색법을 실현하려면 데이터의 저장 및 검색, 즉 2개의 알고리즘이 필요
    - 공간 낭비가 심함
- 검색 알고리즘 중에서도 매우 속도가 빠른 알고리즘이므로, 실제 프로그램에서도 많이 사용

---
참고
- 이것이 취업을 위한 코딩 테스트다 with 파이썬 - 나동빈 저
- [ssongplay/[Python] bisect 라이브러리](https://velog.io/@ssongplay/Python-bisect-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC)
- [dlrmsghks7/탐색 알고리즘을 알아봅시다!!:)](https://velog.io/@dlrmsghks7/%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4)