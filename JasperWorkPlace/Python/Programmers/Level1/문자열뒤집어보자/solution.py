# strings = "abcde"

# arr = sorted(strings, reverse=True)
# k = ""
# for a in arr:
#     k += a
# print(k)


strings = "abcde fghijk lmnop"


result_strings = ""

for i in range(len(strings)-1, -1, -1):
    result_strings += strings[i]

print(result_strings)
