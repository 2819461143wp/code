import random
name_length = 2; #名字长度
north_south=1; #南方1 北方2 分不清3
sex = 1; #男1 女2

cards=[1,2,3,4,1,2,3,4]
for _ in range(name_length):#队首名字长度插入队尾
    cards.append(cards.pop(0))

topthree=cards[:3]
lastfive=cards[3:]#取出队首三个元素
location=random.randint(1,4)
cards=lastfive[:location]+topthree+lastfive[location:]#插入随机位置 队首元素等于队尾元素

qv=cards.pop(0)

top=cards[:north_south]
last=cards[north_south:]
location=random.randint(1,6-north_south)
cards=last[:location]+top+last[location:]#同上

for _ in range (sex):
    cards.pop(0)#除去队首元素
for _ in range(7):
    cards.append(cards.pop(0))#队尾元素 男到-2 女到-3
while len(cards)>1:
    cards.append(cards.pop(0))
    cards.pop(0)
print(cards,qv)#队首元素等于队尾元素

