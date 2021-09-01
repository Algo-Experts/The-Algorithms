# "()()" 또는 "(())()" 는 올바른 괄호입니다.
# ")()(" 또는 "(()(" 는 올바르지 않은 괄호입니다.
# '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# 문자열 s가 올바른 괄호이면 true를 return 하고,
# 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

def solution(s):
    stack = []

    if s[0] == ")":
        return False

    for a in s:
        if a == ')':
            if len(stack) == 0:
                return False
            else:
                del stack[-1]
        else:
            stack += a
    if len(stack) != 0:
        return False
    return True


print(solution("(())()"))
# print(solution("(())()"))

# s = "baababababbb"

# print(s.replace("ab", ""))


# b = s.replace("ab", "")

# while(len(b) > 0):
#     b = s.replace("ab", "")

#     if (set(b) == {'b'}):
#         print(b)
#         break
#     if set(b) == {'a'}:
#         print(b)
#         break
#     if set(b) == {'b', 'a'}:
#         print(b)
#         break


# # print(set(s))
