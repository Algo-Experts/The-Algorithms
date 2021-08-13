# https://www.acmicpc.net/problem/1543

# 문제요약
# 단어 1과 단어 2가 주어짐
# 단어 1안에 단어 2가 몇번 들어가 있는지 찾는 것

# 입력
# 첫째 줄에 문서가 주어진다. 문서의 길이는 최대 2500이다. 둘째 줄에 검색하고 싶은 단어가 주어진다. 이 길이는 최대 50이다. 문서와 단어는 알파벳 소문자와 공백으로 이루어져 있다.

# 출력
# 첫째 줄에 중복되지 않게 최대 몇 번 등장하는지 출력한다.

# 예제 입력 1 
# ababababa
# aba
# 예제 출력 1 
# 2
# 예제 입력 2 
# a a a a a
# a a
# 예제 출력 2 
# 2

# 문제풀이

#값을 받는다 
string = input()
word = input()
count = 0
i = 0
while i <= len(string) - len(word) : # 단어1에서 단어2를 빼준다 빼지 않으면 i의 범위가 초과됨.
    if string[i:i+len(word)] == word : # 0부터 단어2의 길이만큼 잘라서 단어랑 같을경우 +1
        count += 1
        i += len(word)
    else : # 아닐경우 다음 단어로 이동
        i += 1

print(count)
