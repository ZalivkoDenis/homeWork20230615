import random

def task_11_16():
    """1
    11.16. Дан массив целых чисел. Выяснить:
        а) является ли s-й элемент массива положительным числом;
        б) является ли k-й элемент массива четным числом;
        в) какой элемент массива больше: k-й или s-й.
    :return:
    """

    # Подготовка данных
    someList = []
    index = 0
    maxIndex = random.randint(20, 100)
    while index <= maxIndex:
        someList.append(random.randint(-100, 100))
        index += 1

    iK = random.randint(0, maxIndex)
    iS = random.randint(0, maxIndex)

    # Решение задачи
    print(f'Список:\n{someList}\nКоличество элементов: {len(someList)}\nЭлементы:')
    print(f'\tk={iK}, someList[{iK}] = {someList[iK]}')
    print(f'\ts={iS}, someList[{iS}] = {someList[iS]}')

    # a
    print(f'someList[{iS}]', end=' ')
    if someList[iS] > 0:
        print('является положительным числом.')
    else:
        print('не является положительным числом!')

    # б
    print(f'someList[{iK}]', end=' ')
    if someList[iK] % 2 == 0:
        print('является чётным числом.')
    else:
        print('не является чётным числом!')

    # в
    print(f'Из двух элементов someList[{iS}] и someList[{iK}]', end=' ')
    if someList[iK] > someList[iS]:
        print(f'большим является  someList[{iK}].')
    elif someList[iS] > someList[iK]:
        print(f'большим является  someList[{iS}].')
    else:
        print('невозможно определить больший. Элементы равны.')


    return None


def task_11_18():
    """2
    11.18. Дан массив. Все его элементы:
        а) уменьшить на 20;
        б) умножить на последний элемент;
        в) увеличить на число В.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = random.randint(10, 50)
    while index <= maxIndex:
        someList.append(random.randint(-100, 100))
        index += 1
    B = random.randint(-100, 100)
    print(f'Список начальных значений:\n{someList}\nКоличество элементов: {maxIndex+1}')
    print(f'B = {B}')


    # a
    someListA = list(someList)
    index = 0
    while index <= maxIndex:
        someListA[index] -= 20
        index += 1
    print(f'Список (а):\n{someListA}')

    # б
    someListB = list(someList)
    index = 0
    multK = someListB[-1]
    while index <= maxIndex:
        someListB[index] *= multK
        index += 1
    print(f'Массив (б):\n{someListB}')

    # в
    someListV = list(someList)
    index = 0
    while index < maxIndex:
        someListV[index] += B
        index += 1
    print(f'Массив (в):\n{someListV}')

    return None


def task_11_21():
    """3
    11.21. В массиве хранятся сведения о количестве осадков, выпавших за каждый день января.
        Определить общее количество осадков за январь.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = 30
    while index <= maxIndex:
        someList.append(random.randint(0, 30))
        index += 1

    summList = sum(someList)
    print(f'Список:\n{someList}')
    print(f'Сумма всех элементов: {summList}')

    return summList



def task_11_30():
    """4
    11.30. В массиве хранится информация о численности учеников в каждом из 42 классов школы.
        Выяснить, верно ли, что общее число учеников в школе есть четырехзначное число.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = 41
    while index <= maxIndex:
        someList.append(random.randint(15, 35))
        index += 1
    print(f'Список:\n{someList}')

    summList = sum(someList)
    print(f'Общее количество учеников в классе {summList}', end=' ')
    if 999 < summList < 10000:
        print('является четырёхзначным числом.')
    else:
        print('не является четырёхзначным числом.')

    return None


def task_11_36():
    """5
    11.36. Дан массив. Напечатать:
        а) все неотрицательные элементы;
        б) все элементы, не превышающие число 100.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = random.randint(10, 50)
    while index <= maxIndex:
        someList.append(random.randint(-50, 1000))
        index += 1
    print(f'Заданный список:\n{someList}')

    listA = []
    listB = []
    index = 0
    while index < len(someList):
        # a
        if someList[index] >= 0: listA.append(someList[index])
        # b
        if someList[index] <=100: listB.append(someList[index])
        index += 1

    print(f'Список (а):\n{listA}')
    print(f'Список (б):\n{listB}')

    return None


def task_11_39():
    """6
    11.39. Дан массив. Напечатать:
        а) второй, четвертый и т. д. элементы;
        б) третий, шестой и т. д. элементы.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = random.randint(10, 50)
    while index <= maxIndex:
        someList.append(random.randint(-100, 100))
        index += 1
    print(f'Заданный список:\n{someList}')

    # а
    print(f'2,4,...:\n{someList[1::2]}')
    # б
    print(f'3,6,...:\n{someList[2::3]}')

    return None


def task_11_52():
    """7
    11.52. Дан массив целых чисел.
        а) Все элементы, оканчивающиеся цифрой 4, уменьшить вдвое.
        б) Все четные элементы заменить на их квадраты, а нечетные удвоить.
        в) Четные элементы увеличить на a, а из элементов с четными номерами вычесть b.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = random.randint(10, 50)
    while index <= maxIndex:
        someList.append(random.randint(0, 100))
        index += 1
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    print(f'Заданный список:\n{someList}\na = {a}, b = {b}')

    listA = []
    listB = []
    listV = []

    i = 0
    while i < len(someList):
        c = someList[i]
        # а
        if c % 10 == 4:
            listA.append(c//2)
        else:
            listA.append(c)
        # б
        if c % 2 == 0:
            listB.append(c ** 2)
        else:
            listB.append(c*2)
        # в
        if c % 2 == 0: c += a
        if i % 2 == 0: c -= b
        listV.append(c)

        i += 1

    print(f'Список (а). Все элементы, оканчивающиеся цифрой 4, уменьшить вдвое:\n{listA}')
    print(f'Список (б). Все четные элементы заменить на их квадраты, а нечетные удвоить:\n{listB}')
    print(f'Список (в). Четные элементы увеличить на a, а из элементов с четными номерами вычесть b:\n{listV}')

    return None


def task_11_53():
    """8
    11.53. Дан массив целых чисел.
        а) Все элементы, кратные числу 10, заменить нулем.
        б) Все нечетные элементы удвоить, а четные уменьшить вдвое.
        в) Нечетные элементы уменьшить на m, а элементы с нечетными номерами увеличить на n.
    :return:
    """
    # Подготовка данных
    someList = []
    index = 0
    maxIndex = random.randint(10, 50)
    while index <= maxIndex:
        someList.append(random.randint(0, 100))
        index += 1
    m = random.randint(-100, 100)
    n = random.randint(-100, 100)
    print(f'Заданный список:\n{someList}\nm = {m}, n = {n}')

    listA = []
    listB = []
    listV = []

    i = 0
    while i < len(someList):
        c = someList[i]
        # а
        if c % 10 == 0:
            listA.append(0)
        else:
            listA.append(c)
        # б
        if c % 2 == 0:
            listB.append(c // 2)
        else:
            listB.append(c*2)
        # в
        if c % 2 != 0: c -= m
        if i % 2 != 0: c += n
        listV.append(c)

        i += 1

    print(f'Список (а). Все элементы, кратные числу 10, заменить нулем:\n{listA}')
    print(f'Список (б). Все нечетные элементы удвоить, а четные уменьшить вдвое:\n{listB}')
    print(f'Список (в). Нечетные элементы уменьшить на m, а элементы с нечетными номерами увеличить на n:\n{listV}')

    return None