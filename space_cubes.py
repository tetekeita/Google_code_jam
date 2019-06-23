# Google code jam ProblemC.Space Cubes
# For only Small dataset
import math

def subset_from_vector(v, a_set):
    if len(v) != len(a_set):
        return []

    subset = []
    for vi, element in zip(v, a_set):
        if vi == 1:
            subset += [element]
    return subset


def enumerate_all_subsets(K,a_set=['a', 'b', 'c']):
    subsets = [] # 部分集合を保存するためのリスト
    S = [[]] # スタック　
    while len(S) > 0: # スタックが空でない限り以下を繰り返す．
        v = S.pop() # スタックから0-1列を1つ取り出す．
        if len(v) == len(a_set): # 0-1列が集合の要素数と同じ長さならば，
            A=subset_from_vector(v, a_set)
            if len(A)==K:
                subsets += [subset_from_vector(v, a_set)] # その0-1ベクトルが特性列であると見なして，部分集合を作り，保存する．
        else: # 0-1列が集合の要素数よりも短いならば，
            S += [v + [0]] # それに0を追加した列をスタックに入れる．
            S += [v + [1]] # それに1を追加した列もスタックに入れる．
    return subsets # 最後にまとめて，長さがK個の部分集合を返す．



def all_answer(input_file,output_file):
    input=open(input_file,'r')

    output=open(output_file,'w')

    test=int(input.readline().rstrip())# テストケース数

    for t in range(test):
        kazu=input.readline().rstrip().split(" ")# NとKの値をインプット
        N=int(kazu[0])
        K=int(kazu[1])

        cakes=[[0]*2 for i in range(N)]# パンケーキのRとHをいれるための配列を定義

        for i in range(N):# RとKをインプット
            cakeData=input.readline().rstrip().split(" ")
            cakes[i][0]=int(cakeData[0])
            cakes[i][1]=int(cakeData[1])

        menseki_max=0
        shugou=enumerate_all_subsets(K,cakes)# N個からK個選ぶ組み合わせを網羅
        for i in range(len(shugou)):# 最も大きい面積の選び方を見つける
            R_max=0
            sokumenseki=0
            for j in range(len(shugou[i])):# K個の選びかた1つ1つの総面積を求める
                if shugou[i][j][0]>R_max:
                    R_max=shugou[i][j][0]
                sokumenseki+=shugou[i][j][1]*2*math.pi*shugou[i][j][0]
            menseki=sokumenseki+R_max*R_max*math.pi
            if menseki>menseki_max:
                menseki_max=menseki

        output.write('Case\t#')
        output.write(str(t+1))
        output.write(':\t')
        output.write(str(round(menseki_max,9))+'\n')
    input.close()
    output.close()
    return
