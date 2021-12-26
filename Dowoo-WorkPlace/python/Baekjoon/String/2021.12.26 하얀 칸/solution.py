# https://www.acmicpc.net/problem/1100

# 문제요약
# 하얀칸 위에 말이 몇개 있는지 출력

# 입력
# 첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.

# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 1 
# .F.F...F
# F...F.F.
# ...F.F.F
# F.F...F.
# .F...F..
# F...F.F.
# .F.F.F.F
# ..FF..F.
# 예제 출력 1 
# 1
# 예제 입력 2 
# ........
# ........
# ........
# ........
# ........
# ........
# ........
# ........
# 예제 출력 2 
# 0
# 예제 입력 3 
# FFFFFFFF
# FFFFFFFF
# FFFFFFFF
# FFFFFFFF
# FFFFFFFF
# FFFFFFFF
# FFFFFFFF
# FFFFFFFF
# 예제 출력 3 
# 32

# 문제풀이

# 첫제출 답
a = [list(input()) for _ in range(8)]
cnt = 0

for i in range(0,8) :
    for j in range(0,8) :
        if i % 2 == 0 and j % 2 == 0 and a[i][j] == "F":
            cnt += 1
        if i % 2 == 1 and j % 2 == 1 and a[i][j] == "F":
            cnt += 1

print(cnt)

# 코드 줄임 
# if부분에서 공통점을 찾아서 하나로 줄여버림
a = [input() for _ in range(8)]
cnt = 0

for i in range(8) :
    for j in range(8) :
        if i % 2 == j % 2 and a[i][j] == "F":
            cnt += 1
print(cnt)
            
