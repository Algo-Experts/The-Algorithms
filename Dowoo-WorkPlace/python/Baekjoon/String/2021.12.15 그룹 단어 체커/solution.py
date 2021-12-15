# https://www.acmicpc.net/problem/1316

# 문제요약
# 나왔던 단어가 나올경우 단어가 안됨

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 예제 입력 1 
# 3
# happy
# new
# year
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# aba
# abab
# abcabc
# a
# 예제 출력 2 
# 1

# 문제풀이
N = int(input())

cnt = N
for _ in range(N) :
    a = input()
    for i in range(len(a)-1) :
        if a[i] != a[i+1] : # 다음것과 다를경우에
            if a[i+1] in a[:i] : # 현재까지중 같은게 또 있으면 에러
                cnt -= 1 
                break
print(cnt)
            
            

                
            

