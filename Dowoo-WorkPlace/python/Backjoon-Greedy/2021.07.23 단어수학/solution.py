# https://www.acmicpc.net/problem/1339

# 문제요약
# 0~9까지 숫자가 있고 그에 따라 A부터 알파벳 대문자로 이루어져있다.
# 합계의 최대값을 구하기!

# 입력
# 첫째 줄에 단어의 개수 N(1 ≤ N ≤ 10)이 주어진다. 둘째 줄부터 N개의 줄에 단어가 한 줄에 하나씩 주어진다. 단어는 알파벳 대문자로만 이루어져있다. 모든 단어에 포함되어 있는 알파벳은 최대 10개이고, 수의 최대 길이는 8이다. 서로 다른 문자는 서로 다른 숫자를 나타낸다.

# 출력
# 첫째 줄에 주어진 단어의 합의 최댓값을 출력한다.

# 예제 입력 1 
# 2
# AAA
# AAA
# 예제 출력 1 
# 1998

# 예제 입력 2 
# 2
# GCF
# ACDEB
# 예제 출력 2 
# 99437

# 예제 입력 3 
# 10
# A
# B
# C
# D
# E
# F
# G
# H
# I
# J
# 예제 출력 3 
# 45

# 예제 입력 4 
# 2
# AB
# BA
# 예제 출력 4 
# 187

# 문제풀이

#1. 숫자, 문자를 받아서 저장!
num = int(input())
s = []

for _ in range(num):
    s.append(input())

#2. 알파벳은 26개 이므로 26개 저장.
alphabet = [0 for i in range(26)]

#3. 중요도에 따라 알바벳 선정. 
for word in s:
    for i in range(len(word)) :
        alphabet[ord(word[-1]) - ord('A')] += 10** i
        word = word[:-1]

alphabet.sort(reverse = True)

#4. 더해줌!
sum = 0
for i in range(9,-1,-1):
    sum += alphabet[i] * (9-i)

print(sum)

