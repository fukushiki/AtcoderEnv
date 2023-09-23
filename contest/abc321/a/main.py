N= input()
# N = int(N)

max = 9
Ns = list(N)

flag = True
# print(Ns)
for i, n in enumerate(Ns):
    n = int(n)
    if i == 0:
        max = n
    elif max <= n:
        flag = False
        break
    max = n

if flag:
    print("Yes")
else:
    print("No")