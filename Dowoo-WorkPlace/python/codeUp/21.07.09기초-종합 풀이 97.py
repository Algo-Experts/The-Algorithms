# 97번

# 문제
# 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
# 막대를 놓는 방향(d:가로는 0, 세로는 1)과
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

# 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

# 입력 예시   
# 5 5
# 3
# 2 0 1 1
# 3 1 2 3
# 4 1 2 5

# 출력 예시
# 1 1 0 0 0
# 0 0 1 0 1
# 0 0 1 0 1
# 0 0 1 0 1
# 0 0 0 0 1

#풀이1 : 가로와 세로를 입력받고 0으로 가득채운다
h,w = map(int,(input().split()))

a = [[0 for j in range(w+1)] for i in range(h+1)]

#풀이2 : 입력될 갯수를 받고 막대의 길이,방향,좌표를 받는다!
#받고나서 길이만큼 반복하고 방향에 따라서 값을 지정해준다!

n = int(input())

for i in range(n) :
    l,d,x,y = map(int,(input().split()))
    for j in range(l) : 
        if d == 0 :
            a[x][y+j] = 1
        else :
            a[x+j][y] = 1


#풀이3 : 출력!
for i in range(1,h+1) : 
    for j in range(1,w+1) :
        print (a[i][j], end=' ')
    print()                









