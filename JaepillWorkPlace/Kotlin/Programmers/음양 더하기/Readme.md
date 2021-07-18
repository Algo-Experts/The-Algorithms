1. 문제 출처 :https://programmers.co.kr/learn/courses/30/lessons/76501

reduceIndexed() 와 foldIndexed() 를 사용하면 element 의 인덱스 정보를 사용한 동작을 수행할 수 있다.
fold() 는 initial value 를 받아 첫 element 와 함께 동작을 시작하고 reduce() 는 element 의 첫번째, 두번째 element 를 가지고 동작을 시작


### 풀이
1. absolutes: IntArray, signs: BooleanArray로 주어진 배열을 받는다.
2. educeIndexed() 와 foldIndexed()를 이용한다.
3. idx는 인덱스 번호이며, acc는 foldIndexed의 매개변수 (0)으로부터 시작하는 값이고 num은 해당 인덱스의 값이다.

absolutes.foldIndexed(0) { idx, acc, num -> acc + if (signs[idx]) num else -num }
