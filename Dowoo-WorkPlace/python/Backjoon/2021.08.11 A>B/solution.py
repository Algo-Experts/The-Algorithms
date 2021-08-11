a, b = map(int, input().split())
result = 1

while True :
    if a == b :
        break
    elif (b%2 != 0 and b%10 != 1) or (b<a) :
        result = -1
        break
    else :
        if b % 1 == 1 :
            b = b//10
            result += 1
        else :
            b = b // 2
            result +=1

print(result)