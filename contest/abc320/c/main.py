M = int(input())
S1 = input()
S2 = input()
S3 = input()

def mods(t, M):
    mod = divmod(t, M)
    return mod[1]+1


def index_Multi(List,liter):
    #Listはリスト本体・literは検索したい文字
    index_L = []
    for val in range(0,len(List)):
        if liter == List[val]:
            index_L.append(val)
    return index_L


def check(S1, S2, S3, sets):
    min = -1
    S1l = list(S1)
    S2l = list(S2)
    S3l = list(S3)
    for target in sets:
        # 最小インデックスを求める
        index_list=[index_Multi(S1l, target), index_Multi(S2l, target), index_Multi(S3l, target)]
        print(index_list)
        # S1m = mods(t, M)
        # S2m = mods(t, M)
        # S3m = mods(t, M)
        Timer = 0
        fS1 = False
        fS2 = False
        fS3 = False
        
        while(True):
            Mod = mods(Timer, M)
            
            Timer +=1

        

    return min


# 数字の羅列に共通の数字があるかどうかを調べる
sets = list(set(list(S2)) & set(list(S2)) & set(list(S3)))
if len(sets) == 0:
    print(-1)
else :
    result = check(S1, S2, S3, sets)
    print(result)

