"""
В течени практики, мы с вами учились писать
такие фигуры:
=
==
===
====
=====
Для этого мы выясняли какие символы в них есть,
сколько их и как они изменяются и использовали for
Например здесь быд такой код
"""
for i in range(1, 7):
    print(i*"=")
"""
а в таком случае
     =
    ==
   ===
  ====
 =====
======
код выглядед так:
(сколько-то пробелов + сколько-то '=')
"""
for i in range(1, 7):
    print((7-i)*" " + i*"=")


##########################################
# TODO задание 1
##########################################
"""Напищите код, изображающий фигуру
======
 =====
  ====
   ===
    ==
     =
     """
print("Результат задания 1")

for i in range(6, 0, -1):
    print((7-i)*" " + i*"=")


##########################################
# конец задания
##########################################

##########################################
# TODO задание 2
##########################################
"""Напищите код, изображающий фигуру
    =    
   ===   
  =====  
 =======
=========
(подумайте о том, из сокольки частей состоит фигура,
например x*" " + y*"=" + z * " ")
     """
print("Результат задания 2")

for i in range(1, 11, 2):
    print(int((9-i)/2)*" " + i*"=" + int((9-i)/2)*" ")

##########################################
# конец задания
##########################################


##########################################
# TODO задание 3
##########################################
"""Напищите код, изображающий фигуру
=========
 =======
  =====  
   ===
    =
     """
print("Результат задания 3")

for i in range(9, 0, -2):
    print(int((9-i)/2)*" " + i*"=" + int((9-i)/2)*" ")

##########################################
# конец задания
##########################################


##########################################
# TODO задание 4 дополнительное
##########################################
"""Напищите код, любую красивую фигуру по
вашему желанию
     """
print("Результат задания 4")

for j in range(3):
    for i in range(1, 7, 2):
        print(int((5-i)/2)*" " + i*"=" + int((5-i)/2)*" ")
for i in range(2):
    print(2*" " + "=" + 2*" ")

##########################################
# конец задания
##########################################