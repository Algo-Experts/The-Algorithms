# https://www.acmicpc.net/problem/10809

# 문제요약
# 단어가 나오는데 해당 알파벳이 처음 나오는 위치
# 포함되지 않을 경우 -1

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

# 만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.

# 예제 입력 1 
# baekjoon
# 예제 출력 1 
# 1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1

# 문제풀이

# 문자열을 넣었을 경우
s = input()
a = "abcdefghijklmnopqrstuvwxyz"
for i in a:
    print(s.find(i), end = ' ')

# 아스키코드를 이용할 경우
s = input()
a = list(range(97,123))

for x in a :
    print(s.find(chr(x))) 