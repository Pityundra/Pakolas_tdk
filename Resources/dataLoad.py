from Resources.Item.item1D import Item1D
from Resources.Item.item2D import Item2D
from Resources.Item.item3D import Item3D
from Resources.Item.item4D import Item4D
from Resources.Item.item6D import Item6D


def fileRead(fileName):
    # print(fileName)
    f = open(f"{fileName}", "r")
    lines = f.readlines()
    # print(lines)
    firstLine = lines[0].replace('\n', " ").strip().split()
    # print(firstLine[0])
    items = []
    binSize = []

    if firstLine[0] == '1':
        lines.pop(0)
        for line in lines:
            x = line.replace('\n', " ").strip().split()
            if len(x) == 1:
                # print(x)
                binSize = [int(x[0])]

            if len(x) == 2:
                item = Item1D(int(x[0]), int(x[1]))
                items.append(item)

    if firstLine[0] == '2':
        lines.pop(0)
        for line in lines:
            x = line.replace('\n', " ").strip().split()
            if len(x) == 2:
                # print(x)
                binSize = [int(x[0]), int(x[1])]

            if len(x) == 3:
                item = Item2D(int(x[0]), int(x[1]), int(x[2]))
                items.append(item)

    if firstLine[0] == '3':
        lines.pop(0)
        for line in lines:
            x = line.replace('\n', " ").strip().split()
            if len(x) == 3:
                # print(x)
                binSize = [int(x[0]), int(x[1]), int(x[2])]

            if len(x) == 4:
                item = Item3D(int(x[0]), int(x[1]), int(x[2]), int(x[3]))
                items.append(item)

    if firstLine[0] == '4':
        lines.pop(0)
        for line in lines:
            x = line.replace('\n', " ").strip().split()
            if len(x) == 4:
                # print(x)
                binSize = [int(x[0]), int(x[1]), int(x[2]), int(x[3])]

            if len(x) == 5:
                item = Item4D(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]))
                items.append(item)

    if firstLine[0] == '6':
        lines.pop(0)
        for line in lines:
            x = line.replace('\n', " ").strip().split()
            if len(x) == 6:
                # print(x)
                binSize = [int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])]

            if len(x) == 7:
                item = Item6D(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5]), int(x[6]))
                items.append(item)

    f.close()
    return items, binSize