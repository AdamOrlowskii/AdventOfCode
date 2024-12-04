def count():
    list1 = []
    list2 = []
    answer = 0
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
        answer += abs(list1[x] - list2[x])
    print(answer)
    file.close()


if __name__ == '__main__':
    count()
