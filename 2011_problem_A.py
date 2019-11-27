import random

##エネルギーがどこまで通っているかを見つける関数。
def energy_lastIndex(list):
    length = len(list)
    for a in range(length):
        if list[a] == 0:
            #print(str(a-1) + "を返します。")
            return a
    #print("energyは、すべて1です。")
    return length

##ON/OFFリストにおいて、最初の０(つまり、最初のOFF)を見つける。
def snap_firstIndex(list):
    length = len(list)
    for a in range(length):
        if list[a] == 0:
            return a
    #print("snapは、すべて1です。")
    return length


def answer(N, K):
    snap = []#ONならば、１
    energy = []#電力が通っているならば、１
    for i in range(N):
        snap.append(0)
        if(i == 0):
            energy.append(1)
        else:
            energy.append(0)
    snap_length = len(snap)
    #print("初期値snap",snap)
    #print("初期値energy",energy)

    for i in range(K):
        ##まず、ON/OFFを切り替える。
        #0のときできない？
        for j in range(energy_lastIndex(energy)):
            if snap[j] == 0:
                snap[j] = 1
            else:
                snap[j] = 0
        ##次に、変化したON/OFFに対応したエネルギーリストを変更
        #print("途中snap",snap)
        first_zero_index = snap_firstIndex(snap)
        #print("firstは、",first_zero_index)
        #print("snapは、",snap_length)
        if first_zero_index == snap_length:
            for j in range(first_zero_index):
                energy[j] = 1
        else:
            for j in range(first_zero_index + 1):
                energy[j] = 1
            for j in range(first_zero_index + 1, snap_length):
                energy[j] = 0
        #print("途中energy",energy)

    if all(y == 1 for y in energy) == True:
        return "ON"
    else:
        return "0FF"

if __name__ == "__main__":
    '''
    ##本来、ONになる処理。
    N = 4
    K = 47
    on_or_off = answer(N, K)
    print("Case["+str(0)+"]:",on_or_off)
    '''

    for i in range(5):
        N = random.randint(1,30)
        K = random.randint(0,1000)
        print(str(N),str(K) + "で出力します。")
        on_or_off = answer(N, K)
        print("Case["+str(i + 1)+"]:",on_or_off)
