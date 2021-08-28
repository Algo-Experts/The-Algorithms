# https://www.acmicpc.net/problem/15903

# x와 y를 골라서 더하고 덮어씌운다
# 전체 카드의 덧셈 최소화

# 입력
# 첫 번째 줄에 카드의 개수를 나타내는 수 n(2 ≤ n ≤ 1,000)과 카드 합체를 몇 번 하는지를 나타내는 수 m(0 ≤ m ≤ 15×n)이 주어진다.

# 두 번째 줄에 맨 처음 카드의 상태를 나타내는 n개의 자연수 a1, a2, …, an이 공백으로 구분되어 주어진다. (1 ≤ ai ≤ 1,000,000)

# 출력
# 첫 번째 줄에 만들 수 있는 가장 작은 점수를 출력한다.

# 예제 입력 1 
# 3 1
# 3 2 6
# 예제 출력 1 
# 16
# 예제 입력 2 
# 4 2
# 4 2 3 1
# 예제 출력 2 
# 19


# 문제풀이

N, M = map(int, input().split())
cards = list(map(int, input().split()))

for _ in range(M) :
    cards.sort() #오름차순
    sumCard = cards[0] + cards[1] #합
    cards[0] = sumCard # 합을 바꿔줌.
    cards[1] = sumCard

print(sum(cards))
    
    


