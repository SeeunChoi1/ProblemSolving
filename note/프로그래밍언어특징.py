# 루프
sum = 0
for i in range(1, 10+1):
    sum += i
sum = sum(i for i in range(1, 10+1))
sum = sum(range(1, 10+1))

# 제네릭 프로그래밍
# : 파라미터의 타입이 나중에 지정되게 해서 재활용성을 높일 수 있는 프로그래밍 스타일
# 파이썬은 원래 동적 타이핑 언어라 제네릭이 필요없음
from typing import TypeVar
T = TypeVar('T')
U = TypeVar('U')
def are_equal(a : T, b: U) -> bool:
    return a==b
are_equal(10, 10.0)

# 배열 반복
foo = ['A', 'B', 'C']
for f in foo:
    print(f)

# 구조체
from dataclasses import dataclass
@dataclass
class Product:
    weight: int = None
    price: float = None
apple = Product()
apple.price = 10

# 클래스
from dataclasses import dataclass
@dataclass
class Rectangle:
    width: int
    height: int
    def area(self):
        return self.height * self.width
rect = Rectangle(3, 4)
print(rect.area)

