
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
        rec.append([dev,i])
        print(names[i],' should recieve ',dev)
    elif dev <0:
        send.append([-dev,i])
        print(names[i],' should send ',-dev)

rec.sort(reverse=True,key=lambda x:x[0])
send.sort(reverse=True,key=lambda x:x[0])

print()
delta = 0.1
j=0
for i in range(len(rec)):
    while rec[i][0]> delta:
        if j>=len(send):
            break
        if send[j][0] <= rec[i][0]:
            amount = send[j][0]
            rec[i][0] -= send[j][0]
            print(names[send[j][1]],' should pay ',amount,' to ',names[rec[i][1]])
            j+=1
        else:
            amount = rec[i][0]
            send[j][0] -= rec[i][0]
            rec[i][0] = 0
            print(names[send[j][1]],' should pay ',amount,' to ',names[rec[i][1]])


