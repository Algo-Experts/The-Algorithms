1. 문제 출처 :https://programmers.co.kr/learn/courses/30/lessons/12950


### 풀이
충첩 포문을 사용해 연산하는 방법 대신, 람다식을 활용해 배열자체로 연산하는 방법을 사용해 보았다.
첫번쨰의 경우 arr1.size개의 배열의 원소마다 a를 사용해 연산하는데,
두번쨰의 경우 arr1[i].size개의 배열의 각 원소를 b로 받으므로 결국 위의 코드는
for i in 0...arr1.size{
  for j in 0...arr1[i].size{
    arr1[i][j] + arr2[i][j]
  }
}
이나 마찬가지이다.
