import random

array = [["0" for i in range(10)] for j in range(10)]

class Ships:
    # Создаем пространство вокруг коробля, чтобы избежать слияние кораблей
    def free_place(self, l):
        for i in range(10):
            for j in range(10):
                if l[i][j] == 's':
                    if i != 0:
                        if l[i - 1][j] != "s":
                            l[i - 1][j] = '-'
                    if j != 0:
                        if l[i][j - 1] != "s":
                            l[i][j - 1] = '-'
                    if i != 9:
                        if l[i + 1][j] != "s":
                            l[i + 1][j] = '-'
                    if j != 9:
                        if l[i][j + 1] != "s":
                            l[i][j + 1] = '-'

                    if i != 0 and j != 9:
                        l[i - 1][j + 1] = '-'
                    if i != 0 and j != 0:
                        l[i - 1][j - 1] = '-'
                    if i != 9 and j != 9:
                        l[i + 1][j + 1] = '-'
                    if i != 9 and j != 0:
                        l[i + 1][j - 1] = '-'
        return l

    # Создаем четырехпалубный корабль
    def s4(self, l):
        x, y = random.randint(0, 9), random.randint(0, 9)
        line = ["north", "south", "west", "east"]

        if x in [0, 1, 2]:
            line.remove("north")
        if x in [7, 8, 9]:
            line.remove("south")
        if y in [0, 1, 2]:
            line.remove("west")
        if y in [7, 8, 9]:
            line.remove("east")
        ch = line[random.randint(0, len(line) - 1)]
        if ch == "north":
            l[x][y] = 's'
            l[x - 1][y] = 's'
            l[x - 2][y] = 's'
            l[x - 3][y] = 's'
        if ch == "south":
            l[x][y] = 's'
            l[x + 1][y] = 's'
            l[x + 2][y] = 's'
            l[x + 3][y] = 's'
        if ch == "west":
            l[x][y] = 's'
            l[x][y - 1] = 's'
            l[x][y - 2] = 's'
            l[x][y - 3] = 's'
        if ch == "east":
            l[x][y] = 's'
            l[x][y + 1] = 's'
            l[x][y + 2] = 's'
            l[x][y + 3] = 's'
        return l

    # Создаем трёхпалубный корабль
    def s3(self, l):
        while True:
            x, y = random.randint(0, 9), random.randint(0, 9)
            line = ["north", "south", "west", "east"]

            if l[x][y] != "s" and l[x][y] != "-":
                if x in [0, 1]:
                    line.remove("north")
                if x in [8, 9]:
                    line.remove("south")
                if y in [0, 1]:
                    line.remove("west")
                if y in [8, 9]:
                    line.remove("east")
            else:
                continue

            line2 = []
            for i in line:
                if i == "north":
                    if l[x - 1][y] != "-":
                        if l[x - 2][y] != "-":
                            line2.append("north")
                if i == "south":
                    if l[x + 1][y] != "-":
                        if l[x + 2][y] != "-":
                            line2.append("south")
                if i == "west":
                    if l[x][y - 1] != "-":
                        if l[x][y - 2] != "-":
                            line2.append("west")
                if i == "east":
                    if l[x][y + 1] != "-":
                        if l[x][y + 2] != "-":
                            line2.append("east")
            if len(line2) == 0:
                continue
            ch = line2[random.randint(0, len(line2) - 1)]
            if ch == "north":
                l[x][y] = 's'
                l[x - 1][y] = 's'
                l[x - 2][y] = 's'

            if ch == "south":
                l[x][y] = 's'
                l[x + 1][y] = 's'
                l[x + 2][y] = 's'

            if ch == "west":
                l[x][y] = 's'
                l[x][y - 1] = 's'
                l[x][y - 2] = 's'

            if ch == "east":
                l[x][y] = 's'
                l[x][y + 1] = 's'
                l[x][y + 2] = 's'
            return l
            break

    # Создаем двухпалубный корабль
    def s2(self, l):
        while True:
            x, y = random.randint(0, 9), random.randint(0, 9)
            line = ["north", "south", "west", "east"]

            if l[x][y] != "s" and l[x][y] != "-":
                if x in [0, 1]:
                    line.remove("north")
                if x in [8, 9]:
                    line.remove("south")
                if y in [0, 1]:
                    line.remove("west")
                if y in [8, 9]:
                    line.remove("east")
            else:
                continue

            line2 = []
            for i in line:
                if i == "north":
                    if l[x - 1][y] != "-":
                        line2.append("north")
                if i == "south":
                    if l[x + 1][y] != "-":
                        line2.append("south")
                if i == "west":
                    if l[x][y - 1] != "-":
                        line2.append("west")
                if i == "east":
                    if l[x][y + 1] != "-":
                        line2.append("east")

            if len(line2) == 0:
                continue
            ch = line2[random.randint(0, len(line2) - 1)]
            if ch == "north":
                l[x][y] = 's'
                l[x - 1][y] = 's'

            if ch == "south":
                l[x][y] = 's'
                l[x + 1][y] = 's'

            if ch == "west":
                l[x][y] = 's'
                l[x][y - 1] = 's'

            if ch == "east":
                l[x][y] = 's'
                l[x][y + 1] = 's'
            return l
            break

    # Создаем однопалубный корабль
    def s1(self, l):
        while True:
            x, y = random.randint(0, 9), random.randint(0, 9)
            if l[x][y] == "0":
                l[x][y] = 's'
                return l
                break
            else:
                continue

#Отрисовываем корабли
s = Ships()
array = s.s4(array)
array = s.free_place(array)
array = s.s3(array)
array = s.free_place(array)
array = s.s3(array)
array = s.free_place(array)
array = s.s2(array)
array = s.free_place(array)
array = s.s2(array)
array = s.free_place(array)
array = s.s2(array)
array = s.free_place(array)
array = s.s1(array)
array = s.free_place(array)
array = s.s1(array)
array = s.free_place(array)
array = s.s1(array)
array = s.free_place(array)
array = s.s1(array)
array = s.free_place(array)
array1 = [[" " for i in range(10)] for j in range(10)]

#Проверка выйграша
def win(l, l1):
    flag = True
    for i in range(10):
        for j in range(10):
            if l[i][j] == "s" and l1[i][j] != "X":
                flag = False
                break
    return flag

#Отрисовка поля
alf = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К"]
print("_______________Морской Бой_______________")
print("# 1 # 2 # 3 # 4 # 5 # 6 # 7 # 8 # 9 # 10#")
for i in range(10):
    print(alf[i], "{} # {} # {} # {} # {} # {} # {} # {} # {} # {} #".format(array1[i][0], array1[i][1], array1[i][2],
                                                                             array1[i][3], array1[i][4], array1[i][5],
                                                                             array1[i][6], array1[i][7], array1[i][8],
                                                                             array1[i][9]))
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Введите координаты удара (Пример - Б4):")
# Основной цикл программы
while True:
    kords = list(str(input()))
    if len(kords) == 2:
        if kords[0] in alf and kords[1] in nums:
            y = int(kords[1]) - 1
        else:
            print('неверный ход')
            continue
    elif len(kords) == 3:
        if kords[0] in alf and kords[1] == "1" and kords[2] == "0":
            y = 9
        else:
            print("неверный ход")
            continue
    else:
        print("неверный ход")
        continue
    x = alf.index(kords[0])
    if array[x][y] == 's':
        array1[x][y] = 'X'
    else:
        array1[x][
            y] = '*'
    print("# 1 # 2 # 3 # 4 # 5 # 6 # 7 # 8 # 9 # 10#")
    for i in range(10):
        print(alf[i],
              "{} # {} # {} # {} # {} # {} # {} # {} # {} # {} #".format(array1[i][0], array1[i][1], array1[i][2],
                                                                         array1[i][3], array1[i][4], array1[i][5],
                                                                         array1[i][6], array1[i][7], array1[i][8],
                                                                         array1[i][9]))
    if win(array, array1):
        print("WIN")
