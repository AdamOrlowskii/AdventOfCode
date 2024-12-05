def count():
    check = 0
    number = 0
    dampener = 0
    i = 0

    def operate():
        nonlocal dampener, number, check, i
        dampener = 0
        check = 0
        if list1[0] < list1[1]:
            i = 0
            for i in range(len(list1) - 1):
                if list1[i + 1] - list1[i] <= 3 and (list1[i + 1] - list1[i] > 0 and list1[i] != list1[i + 1]):
                    check = 0
                else:
                    check = 1
                    dampener = 1
                    break
            if check == 0:
                number += 1
        elif list1[0] > list1[1]:
            i = 0
            for i in range(len(list1) - 1):
                if list1[i] - list1[i + 1] <= 3 and (list1[i] - list1[i + 1] > 0 and list1[i] != list1[i + 1]):
                    check = 0
                else:
                    check = 1
                    dampener = 1
                    break
            if check == 0:
                number += 1
        return dampener

    file = open("data2.txt", "r")
    list_of_lines = file.readlines()
    for line in list_of_lines:
        list1 = [int(x) for x in line.split()]
        dampener = operate()
        if dampener == 1:
            for y in range(len(list1)):
                temp = list1[y]
                list1.pop(y) # to nie działa jak są powtórzenia np 1 2 2 3
                dampener = operate()
                if dampener == 0:
                    break
                else:
                    list1.insert(y, temp)

    print(number)
    file.close()


if __name__ == '__main__':
    count()
