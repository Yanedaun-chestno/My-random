from MyRandomTeto import myrandom

print(
'''Привет!
Это генератор рандомных чисел
Введите:
0 - получить число из вашего диапазона
1 - получить x чисел из вашего диапазона'''
)
p = input()

if p == 0:
    start, finish = int(input("Введите диапазон от меньшего к большему"))
    print(myrandom(start,finish))
    
elif p == 1:
    start, finish = int(input("Введите диапазон от меньшего к большему"))
    hu = int(input("Сколько вам нужно чисел?"))
    for _ in range(hu):
        print(myrandom(start,finish))