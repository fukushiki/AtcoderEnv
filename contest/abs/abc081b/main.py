N = int(input())
A = list(map(int, input().split()))


def EVEN(list):
    l2 = []
    for l in list:
        if l %2 != 0:
            return list, True
        l2.append(l/2)
    return l2, False


count=0
while(True):
    A, result = EVEN(A)
    if (result):
        break
    count+=1

print(count)