########################################
# задание на While - 1
########################################

print("########################################")
print("задание на While - 1")
print("########################################", "\n")

def SumDist(dist):
    pow = 0
    TotalDist = 0
    l = []
    while(TotalDist < dist):
        TotalDist = TotalDist + 2**pow
        pow = pow + 1
        l.append(TotalDist)
    print("Дистанции за каждую тренировку:")
    print(l)
    print("Спортсмен преодолеет отметку в", dist, "км на", pow, "день")
SumDist(10000)

print("\n")

########################################
# задание на While - 3
########################################

print("########################################")
print("задание на While - 3")
print("########################################", "\n")
i = 1
WorkoutDist = 10
TotalDist = 0
while i <= 30:
    TotalDist = TotalDist + WorkoutDist * 2
    WorkoutDist = 1.15 * WorkoutDist
    i = i + 2
print("За месяц спортсмен преодолеет:", round(TotalDist, 3), "км")
print("\n")

########################################
# задание на While - 4a
########################################

print("########################################")
print("задание на While - 4a")
print("########################################", "\n")

i = 1
WorkoutDist = 10
l = []
while WorkoutDist <= 20:
    WorkoutDist = 1.1 * WorkoutDist
    l.append(round(WorkoutDist, 3))
    i = i + 1
print("Дистанции за каждую тренировку:")
print(l)
print("Спортсмен преодолеет отметку в 20 км/сут на", i, "день")
print("\n")

########################################
# задание на While - 4b
########################################

print("########################################")
print("задание на While - 4b")
print("########################################", "\n")

i = 0
WorkoutDist = 10
TotalDist = 0
l = []
while TotalDist <= 100:
    TotalDist = TotalDist + WorkoutDist
    l.append(round(TotalDist, 3))
    WorkoutDist = 1.1 * WorkoutDist
    i = i + 1
print("Суммарные дистанции за каждые тренировки:")
print(l)
print("Спортсмен преодолеет отметку в 100 км на", i, "день")
print("\n")

########################################
# задание на For - 1
########################################

print("########################################")
print("задание на For - 1")
print("########################################", "\n")

def FibbNum(num):
    first = 1
    second = 1
    temp = 0
    for _ in range(num - 2):
        temp = second
        second = second + first
        first = temp
    return second
print("Элемент:", FibbNum(7))

print("\n")

########################################
# задание на For - 2
########################################

print("########################################")
print("задание на For - 2")
print("########################################", "\n")

def FibbNum2(num):
    first = 1
    second = 1
    third = 1
    temp = 0
    temp1 = 0
    for _ in range(num - 3):
        temp = third
        third = third + second + first
        temp1 = second
        second = temp
        first = temp1
    return third
print("Элемент:", FibbNum2(4))

print("\n")

########################################
# задание на For - 3
########################################

print("########################################")
print("задание на For - 3")
print("########################################", "\n")

def PowNumb(N):
    l = [i * i for i in range(1, N + 1, 2)]
    print(l)
PowNumb(11)

print("\n")

########################################
# задание на For - 4
########################################

print("########################################")
print("задание на For - 4")
print("########################################", "\n")

def SumAdd(a, b):
    sum = 0
    add = 1
    for i in range(a, b + 1, 1):
        sum = sum + i
        add = add * i
    print("Сумма:", sum)
    print("Умножение:", add)
SumAdd(5, 10)

print("\n")

########################################
# задание на For - 5
########################################

print("########################################")
print("задание на For - 5")
print("########################################", "\n")

def CreateLists(a, b):
    if(a % 2 != 0):
        l1 = [i for i in range(a, b + 1, 2)]
        l2 = [i for i in range(a + 1, b + 1, 2)]
    else:
        l1 = [i for i in range(a + 1, b + 1, 2)]
        l2 = [i for i in range(a, b + 1, 2)]
    print("Нечётные", l1)
    print("Чётные", l2)
CreateLists(5, 11)

print("\n")

########################################
# задание на For - 6
########################################

print("########################################")
print("задание на For - 6")
print("########################################", "\n")

l = [2, 3, -12, 0, 3, 93, -7, -33]
def DevLists(l):
    lPos = [i for i in l if i >= 0]
    lNeg = [i for i in l if i < 0]
    print("Положительные:", lPos)
    print("Отрицательные:", lNeg)
DevLists(l)

print("\n")

########################################
# задание Рисовашки - 1
########################################

print("########################################")
print("задание Рисовашки - 1")
print("########################################", "\n")

def DrawRectangle(h, w):
    if((w > 0) & (h > 0)):
        print(w * "*")
        for i in range(1, h - 1):
            print("*" + (w - 2)*" " + "*")
        if(h > 1):
            print(w * "*")
DrawRectangle(5, 5)

print("\n")

########################################
# задание Рисовашки - 2
########################################

print("########################################")
print("задание Рисовашки - 2")
print("########################################", "\n")

def DrawRectangleSymb(h, w, symb):
    strSymb = str(symb)
    if((w > 0) & (h > 0)):
        print(w * strSymb)
        for i in range(1, h - 1):
            print(strSymb + (w - 2)*" " + strSymb)
        if(h > 1):
            print(w * strSymb)
DrawRectangleSymb(5, 5, "5")

print("\n")

########################################
# задание Рисовашки - 3
########################################

print("########################################")
print("задание Рисовашки - 3")
print("########################################", "\n")

def DrawRectangleWidth(h, w, f, symb):
    strSymb = str(symb)
    if ((2*f < h) & (2*f < w) & (w > 0) & (h > 0)):
        for _ in range(f):
            print(w * strSymb)
        for _ in range(1, h - 1):
            print(f * strSymb + (w - 2*f)*" " + f * strSymb)
        if (h > 1):
            for _ in range(f):
                print(w * strSymb)
    else:
        print("Невозможно отрисовать фигуру!")
DrawRectangleWidth(10, 10, 3, "5")

print("\n")
