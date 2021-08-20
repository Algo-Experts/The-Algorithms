import sys

N = int(sys.stdin.readline())
tips = []
sum = 0

for _ in range(N) :
    tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

for i in range(len(tips)) :
    if tips[i]-i >=0 :
        sum += tips[i] -i

print(sum)