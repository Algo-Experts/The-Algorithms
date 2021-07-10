#출력하기
print()

#입력값 받기
a=input()

#정수입력
int()

#실수
float()

#두개 입력받기 *공백기준으로 입력된 값을 나누어 자른다.
a,b = input().split()#split(이안에 구분점을 둘 수 있다)) 

#연이어 출력하기
print(a,a,a) 

#각 문자의 한 문자씩 분리
a=input()
print(a[0]) #첫번째
print(a[1]) #두번째

#10진번은 0~9까지 / 16진법은 0~f까지 / 8진법은 0~7까지
a = input()
b = int(a)  
print('%x'%b)  #16진법 대문자는 X
print('%o'%b) #8진법

#나눈 몫구하기
print(a//b)

#반복하는 법 b를 a만큼 복사출력
print(int(a)*b)

#chr()은 정수를 문자로 변경
print(chr(a))

#응용 다음문자값 구하기 
print(chr(a+1))

#ord()은 문자를 정수로 변경
print(ord(a))

#나눈 나머지값 구하기
print(a%b)

#소수점 n번째까지만 보기
print(format(a,".nf"))

#제곱배 b가 2일 경우는 2배
print(a << b) 

#비교연산 <,>,<=,>=,==,!=

#참거짓 판별
bool() 

#참거짓 바꾸기 not

#비트단위로 not 
print(~a)

#비트단위로 and
print(a&b)

#비트단위로 or
print(a|b)

#비트단위 xor (같은 1일경우는  0으로 반대일경우는 1로)
print(a^b)

#3항 연산자 x if 조건식 else y
print(int(a if (a>=b) else b))


#if문 라인을 잘 맞춰야한다!
#java와 차이점은 :으로 처리됨.
#if문 중 참고사항 70번 문제
a = int(input())

if a//3 == 1 :
    print("spring")
elif a//3 == 2 :
    print("summer")
elif a//3 == 3 :
    print("fall")
else :
    print("winter")


#반복문 while // a가 0이 아닐때 까지 돌아감.
while a!= 0 :
    print(a)

#end='\n' 또는 생략이 줄바꿈이 됨

#range(시작, 끝, 증감)


#배열 안을 가득 채우는 법 
for i in range(20) :
    a.append(0) #0으로 가득채움


#배열 안에 배열을 채우는 법 
#ex) a [[0,0,0],[0,0,0]] 이런식으로 채운다.
for i in range(20) :
    a.append([])
    for j in range(20) : 
        a[i].append(0) #0으로 가득채움

d = [[0 for j in range(20)] for i in range(20)]
#이와 동일한 방법으로 배열안에 배열을  0 으로 채우는 방법이다.


#2차원 배열에 접근법
a[0][0] #이렇게 [][]이런방법으로 진행 이 말은 a리스트에 0번째의 0번째를 불러오라는 말.


# 여러개의 값을 받을때 int로 받는 법!
a = list(map(int, input().split()))