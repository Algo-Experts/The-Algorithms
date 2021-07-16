1. 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68644

### MutableList를 사용하는 이유
1.ArrayList는 sorted()만 존재함
2. sort는 배열을 정렬하고 sorted()는 배열을 정렬한 리스트를 반환


### 풀이
1. 주어진 배열의 모든 원소의 합을 중복없이 오름차순으로 정렬해야 함
2. 2중첩 for문으로 i, j로 인덱스변수 두가지를 사용해 순차탐색을 중첩해서 실행해 모든 경우의 수를 구한다.
3. distinict로 중복을 제거한다
4. 
