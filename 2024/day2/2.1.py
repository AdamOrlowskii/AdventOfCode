def count():
    check = 0
    number = 0
    file = open("data2.txt", "r")
    list_of_lines = file.readlines()
    for line in list_of_lines:
        list1 = [int(x) for x in line.split()]
        if list1[0] < list1[1]:
            for i in range(len(list1) - 1):
                if list1[i + 1] - list1[i] <= 3 and (list1[i + 1] - list1[i] > 0 and list1[i] != list1[i+1]):
                    check = 0
                else:
                    check = 1
                    break
            if check == 0:
                number += 1
        elif list1[0] > list1[1]:
            for i in range(len(list1) - 1):
                if list1[i] - list1[i + 1] <= 3 and (list1[i] - list1[i + 1] > 0 and list1[i] != list1[i+1]):
                    check = 0
                else:
                    check = 1
                    break
            if check == 0:
                number += 1
    print(number)


if __name__ == '__main__':
    count()
