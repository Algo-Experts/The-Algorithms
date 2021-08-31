# https://www.acmicpc.net/problem/1700

# 문제요약
# 멀티탭과 코드들이 있음 
# 최소로 코드를 뽑았다가 끼는 방법을 구하는것

# 입력
# 첫 줄에는 멀티탭 구멍의 개수 N (1 ≤ N ≤ 100)과 전기 용품의 총 사용횟수 K (1 ≤ K ≤ 100)가 정수로 주어진다. 두 번째 줄에는 전기용품의 이름이 K 이하의 자연수로 사용 순서대로 주어진다. 각 줄의 모든 정수 사이는 공백문자로 구분되어 있다. 

# 출력
# 하나씩 플러그를 빼는 최소의 횟수를 출력하시오. 

# 예제 입력 1 
# 2 7
# 2 3 2 3 1 2 7
# 예제 출력 1 
# 2

# 문제풀이
# 와 너무 어려웠다...

import sys

#값을 받아줌
N, K = map(int, sys.stdin.readline().split())
plug = list(map(int, sys.stdin.readline().split()))
tap = []
count = 0 # 결과값
swap = 0 # 인덱스를 구하기 위한 값
top = 0 # 몇번이나 있는가

for i in range(K) :
    if plug[i] in tap : # 꽂혀 있을경우 패스!
        continue

    elif len(tap) < N : # 안꽂혀있고 탭이 비었으면 추가!
        tap.append(plug[i])
        continue

    else : # 꽉차있을 경우!
        for j in tap : # 탭을 반복시킴
            if j not in plug[i:] : # 앞으로 더 꼽는게 없을 경우 바로 교체시킴
                swap = j
                break
            elif plug[i:].index(j) > top : # 꼽을 게 더 있을 경우 인덱스 값으로 비교
                swap = j # 교체
                top = plug[i:].index(j)
        tap[tap.index(swap)] = plug[i] # 교체시킴
        swap = top = 0 # 초기화
        count += 1 # 교체했기때문에 1추가

print(count)