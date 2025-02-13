#1031: 스타 대결


jiminPeopleNum, hansuPeopleNum = map(int,input("").split(" "))

jiminBattleNumList = list(map(int, input().split(' ')))
hansuBattleNumList = list(map(int, input().split(' ')))


jiminBattleNumDict = {i: jiminBattleNumList[i] for i in range(len(jiminBattleNumList))}
hansuBattleNumDict = {i: hansuBattleNumList[i] for i in range(len(hansuBattleNumList))}

jiminBattleNumDictSorted = dict(sorted(jiminBattleNumDict.items(), key = lambda item:item[1], reverse=True))
hansuBattleNumDictSorted = dict(sorted(hansuBattleNumDict.items(), key = lambda item:item[1], reverse=True))

battleTable = [[0 for i in jiminBattleNumList] for j in hansuBattleNumList]
#print(battleTable)

# 불가 케이스 제외
if sum(jiminBattleNumList) != sum(hansuBattleNumList) :
    print("-1")
else:
    for i in jiminBattleNumDictSorted:
        for j in hansuBattleNumDictSorted:
            if jiminBattleNumList[i] > 0 and hansuBattleNumList[j] > 0:
                battleTable[i][j] = 1
                jiminBattleNumList[i]-=1
                hansuBattleNumList[j]=-1
            elif jiminBattleNumList[i]<=0:
                break
            
            
            
print(battleTable)