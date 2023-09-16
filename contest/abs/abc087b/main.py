A = int(input())
B = int(input())
C = int(input())

X = int(input())


# X円となる組み合わせの表を作りたい
A_val, B_val, C_val = [500, 100, 50]
# print(int(X/A_val))
A_MAX = min(int(X/A_val), A)
# print(int(X/B_val))
B_MAX = min(int(X/B_val), B)
# print(int(X/C_val))
C_MAX = min(int(X/C_val), C)

# print(A_MAX, B_MAX, C_MAX)

# for a in range(10):
#     print(a)
# print(A_MAX)
# for a in range((B_MAX+1 if B_MAX!=0 else 0)):
#     print(f"b : {a}")



count=0
for a in range((A_MAX+1 if A_MAX else 0)):
    sum = A_val*a
    if sum == X :
        count+=1
    elif sum < X:
        for b in range((B_MAX+1 if B_MAX else 0)):
            sum += B_val*b
            if sum == X :
                count+=1
            elif sum<X:
                for c in range((C_MAX+1 if C_MAX else 0)):
                    sum += C_val*c
                    if sum == X:
                        count+=1
                        # print(f"{a}, {b}, {c}")
print(count)