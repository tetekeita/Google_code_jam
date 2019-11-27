## P以上B以下の素因数を抽出する関数。
def soinsu(P_kari, B_kari):
  soinsuList = []
  for i in range(P_kari, B_kari + 1):
    flag = 0
    for j in range(1, i + 1):
      if i % j == 0:
        flag = flag + 1
    if flag == 2:
      soinsuList.append(i)
  return soinsuList

##3入力で何個の集合があるか判定する。
def answer(A, B, P):
  soinsulist = soinsu(P, B)
  kazuList = []
  for i in range(A, B+1):
    kazuList.append(i)
  #print(kazuList)
  sumShugo = len(kazuList)
  for soinsuu in soinsulist:
    flag = 0
    for kazu in kazuList:
      if kazu % soinsuu == 0:
        flag = flag + 1
    flag = flag - 1
    sumShugo = sumShugo - flag
  return sumShugo

if __name__ == "__main__":
  print(answer(10,20,5))
