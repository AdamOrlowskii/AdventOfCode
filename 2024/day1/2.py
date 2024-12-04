def count():
    list1 = []
    list2 = []
    answer1 = 0
    counter = 0
    answer2 = 0
    file = open("data.txt", "r")
    for line in file:
        column1, column2 = line.split()
        list1.append(column1)
        list2.append(column2)
    list1.sort()
    list2.sort()
    for x in range(len(list1)):
        list1[x] = int(list1[x])
        list2[x] = int(list2[x])
        answer1 += abs(list1[x] - list2[x])
    print(answer1)
    for x in range(len(list1)):
        for y in range(len(list1)):
            if list1[x] == list2[y]:
                counter += 1
        answer2 += (list1[x] * counter)
        counter = 0
    print(answer2)


if __name__ == '__main__':
    count()
