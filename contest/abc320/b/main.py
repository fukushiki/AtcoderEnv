S = input()
# length = 1
leng = len(S) + 1

# while length <= leng:
#     Sa = S[:length]
#     if Sa == Sa[::-1]:
#         longest = Sa
#     length += 1

# print(len(longest))
longest=0

for i in range(leng):
    for s in range(i+1, leng):
        # print(i, s)
        Sa = S[i:s+1]
        if Sa == Sa[::-1]:
            longest = max(len(Sa),longest)
print(longest)
