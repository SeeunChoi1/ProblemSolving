# 탐색

* 검색의 다른 명칭이 탐색  
* 검색 엔진에는 엔진이라는 이름이 붙어 있는데, 이를 엄밀하게 말하면 원하는 정보를 사람을 대신하여 찾아 주는 데이터 탐색 프로그램  
    ➡️ 데이터 탐색 프로그램에서 사용하고 있는 알고리즘이 바로 탐색 알고리즘   
* 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정  
    * 탐색에서 빠르다는 것은 **데이터가 많고 원하는 데이터가 배열의 끝 부분에 저장**되어 있는 경우를 말하는 것  
* 대표적인 알고리즘으로는 DFS와 BFS가 있음
    * 그래프 탐색
    * DFS와 BFS가 그래프에만 사용되지는 않는다 [예시)백준_연산자 끼워 넣기](https://www.acmicpc.net/problem/14888)

## DFS / BFS
* [DFS](./%ED%83%90%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/DFS.md)
* [BFS](./%ED%83%90%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/BFS.md)

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
- [이진 탐색](./%ED%83%90%EC%83%89_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/binary_search.md)
- 시간복잡도 O(logN)

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
- [dlrmsghks7/탐색 알고리즘을 알아봅시다!!:)](https://velog.io/@dlrmsghks7/%ED%83%90%EC%83%89-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%84-%EC%95%8C%EC%95%84%EB%B4%85%EC%8B%9C%EB%8B%A4)

[🏠 목록으로](/README.md)