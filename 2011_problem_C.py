def answer(R, k, glist):
    ##R回ジェットコースターは動く。
    money = 0
    for i in range(R):
        print(str(i + 1)+"回目")
        sum = 0
        for j in range(len(glist)):
            first = int(glist[0])
            sum = sum + first
            #print(sum)
            if sum > k:
                sum = sum - first
                print(glist)
                print("beyondBREAK")
                print("現在の合計は",money)
                break
            elif sum == k:
                a = glist.pop(0)
                money = money + int(a)
                glist.append(a)
                print(glist)
                print("equalBREAK")
                print("現在の合計は",money)
                break
            else:
                a = glist.pop(0)
                glist.append(a)
                money = money + int(a)
                print("money",money)
            #if j + 1 == len(glist)
        if i + 1 == R:
            print("最終",glist)
            return money

def all_answer(inputfile, outputfile):
    input = open(inputfile, "r")
    output = open(outputfile, "w")

    test = int(input.readline().rstrip())##テストケース

    for i in range(test):
        kazu = input.readline().rstrip().split(" ")
        R = int(kazu[0])
        k = int(kazu[1])
        N = int(kazu[2])
        glist = input.readline().rstrip().split(" ")
        allanswer = answer(R, k, glist)
        output.write("Case\t#" + str(i + 1))
        output.write(":\t")
        output.write(str(allanswer)+"\n")
    input.close()
    output.close()
    return

if __name__ == "__main__":
    #print(answer(5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3]))
    all_answer("problem_3_small.in", "problem_3_small.out")
