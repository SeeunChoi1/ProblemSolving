# 힙 / 우선순위큐

## 힙 (Heap)
- 우선순위 큐(Priority Queue)를 구현하기 위하여 사용하는 자료구조
- [완전 이진 트리](../dataStructure/tree.md)의 일종
- 여러 개의 값들 중에서 최댓값과 최솟값을 빠르게 찾아내도록 만들어진 자료구조
- 일종의 반 정렬 상태를 유지함

### 힙의 종류
1. 최대 힙 MinHeap
2. 최소 힙 MaxHeap
(참고 : [힙이란](https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html))

## 우선순위 큐 (Priority Queue)
- 우선순위 큐 : 우선순위가 가장 높은 데이터를 가장 먼저 삭제

>**추출 데이터 비교**
>|자료구조|추출되는 데이터|
>|------|-----------|
>|스택(Stack)|가장 나중에 삽입된 데이터|
>|큐(Queue)|가장 먼저 삽입된 데이터|
>|우선순위 큐(Priority Queue)|가장 우선순위가 높은 데이터|

- 파이썬에서는 heapq 라이브러리 사용
- 대부분의 프로그래밍 언어에서는 우선순위 큐 라이브러리에 데이터의 묶음을 넣으면, 첫 번재 원소를 기준으로 우선순위를 설정함

- 내부적으로 MinHeap, MaxHeap을 이용함
    - 파이썬, 자바에서는 MinHeap을 이용하여 우선순위 라이브러라기 구현되어있음
    - C++에서는 MinHeap을 이용하여 우선순위 라이브러리가 구현되어 있음
- **MinHeap을 MaxHeap처럼 쓰려면 음수(-)를 붙여서 사용하면 됨**

>**우선순위 큐 구현방식 비교**
>|우선순위 큐 구현방식|삽입 시간|삭제시간|
>|------|-----------|------|
>|리스트|o(1)|o(N)|
>|힙(Heap)|o(logN)|o(logN)|

[🏠 목록으로](/README.md)