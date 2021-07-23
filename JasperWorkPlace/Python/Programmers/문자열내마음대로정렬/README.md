1. 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12915

### 람다 표현식

> 람다 표현식 이란?

인공지능 분야나 Auto CAD 라는 설계 프로그램에서 쓰이는 Lisp 라는 언어에서 물려 받았다고 한다.

함수를 딱 한 줄 만으로 만들게 해준다.

> 형식은 ?

lamda 인자 : 표현식

> > 두수를 더한 함수로 예시

> > > 일반 함수

```python

def hap( x , y ){
    return x + y
}

hap(10, 20)

# 30

```

> > > 람다 형식

```python

(lambda x, y: x + y)(10, 20)

# 30

# 함수 이름이 없넹 ..?

```

> > Map() 함수

map(함수 , 리스트)

이 함수는 함수와 리스트를 인자로 받는다.

```python

# python 2
map(lambda x: x ** 2 , range(5))

# python 3

list(map(lambda x: x ** 2 , range(5)))

# 2 와 3 모두 [0,1,4,9,16]

```

> > reduce() 함수

reduce(함수, 시퀸스)

시퀸스(문자열, 리스트, 튜플)의 원소들을 누적적으로 함수를 적용시킨다고 한다.

```python
# python 3 에서는 써야 한다.
from functools import reduce
reduce(lambda x, y : x + y , [0,1,2,3,4])

# 10

# 위의 예제는 먼저 0과 1을 더하고, 그 결과에 sequence 에 있는 값을 차례로 더해주는 값을 이야기한다.

reduce(lambda x, y : y + x , 'abcde')

# 'edcba'

```

> > filter()

filter(함수, 리스트)

```python

list(filter(lambda x : x <5 , range(10)))
[0,1,2,3,4]



```
