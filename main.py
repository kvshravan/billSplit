from heapq import heapify,heappush,heappop

n = int(input('Enter number of ppl: '))
arr,names = [],[]
for i in range(n):
    name =   input(f'Enter person {i+1} name: ')
    expense = int(input(f'Enter {name}\'s expense: '))
    arr.append(expense)
    names.append(name)
    print()

for i in range(len(arr)):
    print('Money spent by ',names[i],'-',arr[i])
mean = sum(arr)/len(arr)

print('\nMEAN',mean,'\n')

send,rec = [],[]

for i in range(len(arr)):
    dev = arr[i]-mean
    if dev>0:
        rec.append((-dev,i))
        print(names[i],' should recieve ',dev)
    elif dev <0:
        send.append((dev,i))
        print(names[i],' should send ',-dev)

heapify(rec),heapify(send)
print()
printDict = {}
delta = 0.1
while len(rec):
    hrec,hsend = heappop(rec),heappop(send)
    maxrec,maxsend = (-hrec[0],hrec[1]),(-hsend[0],hsend[1]),
    if maxsend[0] > maxrec[0]:
        if maxsend[1] not in printDict:
            printDict[maxsend[1]] = [(maxrec[0],maxrec[1])]
        else:
            printDict[maxsend[1]].append((maxrec[0],maxrec[1]))
        elem = (-(maxsend[0]-maxrec[0]),maxsend[1])
        heappush(send,elem)
    else:
        if maxsend[1] not in printDict:
            printDict[maxsend[1]] = [(maxsend[0],maxrec[1])]
        else:
            printDict[maxsend[1]].append((maxsend[0],maxrec[1]))
        elem = (-(maxrec[0]-maxsend[0]),maxrec[1])
        if -elem[0] > delta:
            heappush(rec,elem)

for key in printDict:
    for amount,rec in printDict[key]:
        print(f'{names[key]} should pay {amount} to {names[rec]}')
