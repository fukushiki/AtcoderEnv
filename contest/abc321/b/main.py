# N, X =  input().split()
# N = int(N)
# X = int(X)
# As = list(map(int, input().split()))

# Asuminit = sum(As)
# Asmax = max(As)
# Asmin = min(As)

# As.remove(Asmax)
# As.remove(Asmin)
# # print(As)
# Asum = sum(As)
# # print(Asum)
# result = X - Asum

# if N==3 and Asuminit >= X:
#     print(0)
# elif N==3 and X-Asuminit > 100:
#     print(X-Asuminit)

# elif result > 100:
#     print(-1)
# else:
#     print(result)

N, X = map(int, input().split())
As = list(map(int, input().split()))

# 既に取った N-1 ラウンドのスコアの合計を計算
Asum = sum(As)

# 最大値と最小値を取得
Asmax = max(As)
Asmin = min(As)

# 最終結果の最小値を計算
result = X - (Asum + Asmin)

if result > 100 or result < 0:
    print(-1)
else:
    print(result)
