# https://www.acmicpc.net/problem/10808

# 문제요약
# 단어가 몇개인지 구하는 프로그램

# 입력
# 첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

# 출력
# 단어에 포함되어 있는 a의 개수, b의 개수, …, z의 개수를 공백으로 구분해서 출력한다.

# 예제 입력 1 
# baekjoon
# 예제 출력 1 
# 1 1 0 0 1 0 0 0 0 1 1 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0

# 문제풀이

s = input()
a = "abcdefghijklmnopqrstuvwxyz"
for i in range(len(a)):
    print(s.count(a[i]), end = ' ')
    
    
