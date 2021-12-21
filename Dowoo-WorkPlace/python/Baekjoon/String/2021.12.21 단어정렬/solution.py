# https://www.acmicpc.net/problem/1181

# 문제요약
# 중복제거
# 길이가 짧은 것부터
# 길이가 같으면 사전순으로 출력

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.

# 예제 입력 1 
# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours
# 예제 출력 1 
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate

# 문제풀이
N = int(input())
a = [input() for _ in range(N)]
a_l = list(set(a)) # set 중복제거
a_l.sort(key = lambda x : (len(x), x)) # 길이순 / 사전단어순으로 정렬
print(*a_l)
