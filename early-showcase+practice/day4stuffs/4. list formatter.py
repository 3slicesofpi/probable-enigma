# formats lists
theList = [1,2,3,4,5,6,7,8,9,1,11,22,33,44,55,66,77,88,99,20,111,222,333,444,555,666,777,888,999,300]

theListLen = len(theList)
newListPageCount = 0
newList = [[]]
for here in range(0,theListLen):
    if here%10 == 0:
        newList.append([])
        newListPageCount += 1
    newList[newListPageCount].append(theList[here])
newList.remove([])

# frontend
pageSelected = 1
while pageSelected > -1:
    for here in newList[pageSelected-1]:
        print(here)
    print('you are at page',str(pageSelected),'out of',newListPageCount)
    clientInput = input('press a number to change page OR press e to exit.')
    try:
        if clientInput == 'e':
            pageSelected = -1
        else:
            pageSelected = int(clientInput)
    except:
        print('caught err')
        pass