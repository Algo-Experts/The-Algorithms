# https://www.acmicpc.net/problem/1764

# 문제요약
# 둘다 해당하는 사람을 구하는 것

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 예제 입력 1 
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton
# 예제 출력 1 
# 2
# baesangwook
# ohhenrie

# 문제풀이
# 사전순으로 출력한다
# 처음에 다른 방법으로 했는데 시간 초과가 계속 걸림
# &로 교집합을 사용하여 처리함 
# set으로 중복 제거

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = [input().strip() for _ in range(N)]
B = [input().strip() for _ in range(M)]
res = sorted(list(set(A)&set(B)))
print(len(res),*res,sep="\n")

