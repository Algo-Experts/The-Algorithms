# https://www.acmicpc.net/problem/2720

# 문제요약
# 거스름돈 문제

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 거스름돈 C를 나타내는 정수 하나로 이루어져 있다. C의 단위는 센트이다. (1달러 = 100센트) (1<=C<=500)

# 출력
# 각 테스트케이스에 대해 필요한 쿼터의 개수, 다임의 개수, 니켈의 개수, 페니의 개수를 공백으로 구분하여 출력한다.

# 예제 입력 1 
# 3
# 124
# 25
# 194
# 예제 출력 1 
# 4 2 0 4
# 1 0 0 0
# 7 1 1 4

# 문제풀이

# 1.케이스갯수를 받고 코인 리스트 만듬
T = int(input())
coins = [25, 10, 5, 1]

# 2. 리스트 만들고 거스름돈 숫자를 받음
for i in range(T) :
    count = []
    C = int(input())
    # 3. 코인 나눠서 값을 리스트에 담아둠.
    for i  in range(len(coins)) :
        count.append(C // coins[i])
        C = C%coins[i]
    # 4. 리스트 출력
    for c in count :
        print(c, end=" ")
    print()


    