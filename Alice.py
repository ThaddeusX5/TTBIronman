import math
fr=open('Alice29.txt','r',encoding='UTF-8')
content=fr.readlines()
contentlines=''

characters=[]
rate={}

for line in content:
    line=line.strip()
    if len(line)==0:
        continue
    contentlines=contentlines+line

    for x in range(0,len(line)):
        if not line[x] in characters:
            characters.append(line[x])
        if line[x] not in rate:
            rate[line[x]]=1
        rate[line[x]]+=1
rate=sorted(rate.items(),key=lambda e:e[1],reverse=True)

print('全文共有%d个字'%len(contentlines))
print('一共有%d个不同的字'%len(characters))
print()

for i in rate:
    print("[",i[0],"]共出现",i[1],"次")
    print("[",i[0],"]概率为",i[1]/len(contentlines))

fr.close
