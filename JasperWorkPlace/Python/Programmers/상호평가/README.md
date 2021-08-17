1. 문제출처 : https://programmers.co.kr/learn/courses/30/lessons/83201?language=python3

2. 다른 사람의 풀이 중 한줄 풀이한 사람의 코드 보면서 같이 공부 할것

📌 내가 원하는 값의 index 를 여러개 들고 올 수 있는 방법

```pyhton
    # filter 사용
    list(filter(lambda e:lis[e] == 1, range(len(lis))))
    [0, 2]
    # enumerate 사용
    [i for i, ele in enumerate(lis) if ele == 1]
    [0, 2]
```
