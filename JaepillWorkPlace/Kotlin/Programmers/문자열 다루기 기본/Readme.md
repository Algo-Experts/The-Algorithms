1. 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12918

### filter
: predicate 형태의 람다식을 인자로 받아 collection의 원소를 조건에 맞게 필터링 해 줍니다.

### isDigit()
: Returns true if this character (Unicode code point) is a digit.


### 문제 풀이
1. filter를 사용하여 isDigit()으로 '정수인 문자의 갯수'를  카운트 하여 결과를 length에 저장한다.
1.1 만약 정수가 섞여있다면, 입력받은 문자열과 길이가 다를것이다.
2. 길이가 4 또는 6이고 입력받은 문자열의 길이가 length의 길이와 같다면 true, 아니면 false를 반환한다.

