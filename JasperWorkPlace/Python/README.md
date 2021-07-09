## Python Useful Method

#### 🙋‍♂️ 중요 알고리즘 유형 정리

1. [Greedy](https://github.com/jasper-oh/coding-test-algorithm)
2. [DFS/BDS](https://github.com/jasper-oh/coding-test-algorithm)
3. [Sort](https://github.com/jasper-oh/coding-test-algorithm)
4. [Binary Searching](https://github.com/jasper-oh/coding-test-algorithm)
5. [Dynamic Programming](https://github.com/jasper-oh/coding-test-algorithm)
6. [Short Path](https://github.com/jasper-oh/coding-test-algorithm)
7. [Graph](https://github.com/jasper-oh/coding-test-algorithm)

#### 🙋‍♂️ Context

1. 문자열, 숫자열
2. ...

#### 🙋‍♂️ 중요 메서드 정리 ( 추후 늘어나면 PDF 정리 예정 )

2021-07-01

count(n) -> 해당 배열 속에 n 이 몇개 들어있는지 확인해 주는 메소드
[확인](https://www.geeksforgeeks.org/python-list-function-count/)

2021-07-02

배열의 중복을 제거 할때는 list(set(array)) 로 집합 형태로 변환 한 후에 다른 배열로 만들어 버리면 간단하다.

2021-07-05

a = bin(arr1[i] | arr2[i])[2:]

10 진수를 2진수로 바꾼 다음, or 연산을 처리해준다.

🐬 and operator => x & y
🐬 not operator => ~ x
🐬 XOR operator => x ^ y

2021-07-09

```python

#  재미 삼아 만들어 본해당 list 안에 있는 원소가 list 인지 아닌지 판단한다음
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
