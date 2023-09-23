def finder(K):
    count = 10
    result = 10

    if K < 11:
        return K - 1  # 1から10までの数はそのまま返す

    N = 11
    while count < K:
        
        Ns = str(N)
        flags = all(int(Ns[i]) > int(Ns[i+1]) for i in range(len(Ns)-1))
        if flags:
            count += 1
            result = N
        N += 1

    return result

K = int(input())
result = finder(K)
print(result)
