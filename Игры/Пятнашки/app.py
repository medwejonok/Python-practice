import random

#Создаем и перемешиваем массив чисел
array = [i for i in range(1,16)]
array.append("#")
random.shuffle(array)

#Подготавливаем значения для отрисовки поля
def proverka_probelov(l):
    array2 = []
    for i in range(len(l)):
        if l[i] == "#":
            array2.append("   ")
            continue
        elif l[i] <= 9:
            array2.append(str(" {} ".format(l[i])))
        else:
            array2.append(str(" {}".format(l[i])))
    return array2

#Отрисовываем поле
def pole(l):
    print("#"*17)
    print("#{}#{}#{}#{}#".format(l[0],l[1],l[2],l[3]))
    print("#{}#{}#{}#{}#".format(l[4],l[5],l[6],l[7]))
    print("#{}#{}#{}#{}#".format(l[8],l[9],l[10],l[11]))
    print("#{}#{}#{}#{}#".format(l[12],l[13],l[14],l[15]))
    return "#"*17
    
#Проверка возможности хода
def check_step(index):
    if index in [0,3,12,15]:
        if index == 0:
            s = ["s","d"]
        if index == 3:
            s = ["a","s"]
        if index == 12:
            s = ["w","d"]
        if index == 15:
            s = ["w","a"]
    elif index in [1,2,4,7,8,11,13,14]:
        if index in [1,2]:
            s = ["s","a","d"]
        if index in [4,8]:
            s = ["s","d","w"]
        if index in [7,11]:
            s = ["a","s","w"]
        if index in [13,14]:
            s = ["w","a","d"]
    else:
        s = ["w","a","s","d"]

    return s

#Проверка выйграша
def win(l):
    l1 = []
    for i in range(16):
        if l[i] !="#":
           l1.append(l[i]) 
    l2 = sorted(l1)
    if l1 == l2 and l[-1] == "#":
        return True
    return False

#Приветствие
print('====Пятнашки=====')
#Основной цикл игры
print(pole(proverka_probelov(array)))
while True:
    if win(array):
        print("WIN!")
        break
    step = str(input())
    step.lower()
    index = array.index("#")
    if step in check_step(index):
        if step == "w":
            array[index],array[index-4] = array[index-4],array[index]
        if step == "a":
            array[index],array[index-1] = array[index-1],array[index]
        if step == "d":
            array[index],array[index+1] = array[index+1],array[index]
        if step == "s":
            array[index],array[index+4] = array[index+4],array[index]
                  
        print(pole(proverka_probelov(array)))
    else:
        print("невозможный ход")
