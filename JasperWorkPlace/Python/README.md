## Python Useful Method

### 🙋‍♂️ 중요 알고리즘 유형 정리

1. [Greedy](https://github.com/jasper-oh/coding-test-algorithm)
2. [DFS/BDS](https://github.com/jasper-oh/coding-test-algorithm)
3. [Sort](https://github.com/jasper-oh/coding-test-algorithm)
4. [Binary Searching](https://github.com/jasper-oh/coding-test-algorithm)
5. [Dynamic Programming](https://github.com/jasper-oh/coding-test-algorithm)
6. [Short Path](https://github.com/jasper-oh/coding-test-algorithm)
7. [Graph](https://github.com/jasper-oh/coding-test-algorithm)

### 🙋‍♂️ Context

1. 중요메서드 정리
2. 람다표현식
3. ...

### 🙋‍♂️ 중요 메서드 정리 ( 추후 늘어나면 PDF 정리 예정 )

#### 2021-07-01

count(n) -> 해당 배열 속에 n 이 몇개 들어있는지 확인해 주는 메소드
[확인](https://www.geeksforgeeks.org/python-list-function-count/)

#### 2021-07-02

배열의 중복을 제거 할때는 list(set(array)) 로 집합 형태로 변환 한 후에 다른 배열로 만들어 버리면 간단하다.

#### 2021-07-05

a = bin(arr1[i] | arr2[i])[2:]

10 진수를 2진수로 바꾼 다음, or 연산을 처리해준다.

🐬 and operator => x & y
🐬 not operator => ~ x
🐬 XOR operator => x ^ y

#### 2021-07-09

```python

#  재미 삼아 만들어 본 해당 list 안에 있는 원소가 list 인지 아닌지 판단한다음
#  list 라면, 내부로 진입하며, 만약 list 형이 아니라면,
#  출력 하는 형태의 매소드
var = [1, 2, ['a', 'b', ['Dream', "TRUE"]]]


def getArrayElement(var):
    for i in range(len(var)):
        if type(var[i]) != list:
            print(var[i])
        else:
            for j in range(len(var[i])):
                if type(var[i][j]) != list:
                    print(var[i][j])
                else:
                    for k in range(len(var[i][j])):
                        print(var[i][j][k])
```

#### 2021-08-31

JOIN 함수 정리
문자열을 다룰때 유용하게 사용되는 함수.

```python

'구분자'.join(list)

'_'.join(["something" , "hello"])

# something_hello

```

#### 2021-09-01

Numpy 정리

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

filter(함수 , 리스트)

리스트에 들어있는 원소들을 함수에 적용시켜서 결과가 참인 값들로 새로운 리스트를 만들어 준다. 0 부터 9 까지의 리스트 중에서 5보다 작은 것만 돌려 주는 예제

```python
# python 2
filter(lambda x : x < 5 ,range(10))

# python 3
list(filter(lambda x : x < 5 ,range(10)))

#  [0,1,2,3,4]


```
