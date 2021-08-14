# https://www.acmicpc.net/problem/2810

# 문제요약
# 일반석과 커플석이 있음 양 옆에  컵홀더가 있는데 컵홀더를 못쓰는 사람의 수를 구하는 것

# 입력
# 첫째 줄에 좌석의 수 N이 주어진다. (1 ≤ N ≤ 50) 둘째 줄에는 좌석의 정보가 주어진다.

# 출력
# 컵을 컵홀더에 놓을 수 있는 최대 사람의 수를 출력한다.
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# SLLS
# 예제 출력 2 
# 4
# 예제 입력 3 
# 9
# SLLLLSSLL
# 예제 출력 3 
# 7

# 문제풀이

# 값을 받아준다.
# 커플석이 두팀일 경우 -1 세팀이면 -2가 되는 규칙을 발견함.

N = int(input()) 
member = input() 
count = member.count('LL') #LL이 몇개인지 카운트

if (count <= 1): 
    print(len(member)) #커플석이 1개 이하면 모두다 사용가능
else: 
    print(len(member) - count + 1) #커플석이 2개 이상이면 -1씩 계속 차감됨.



