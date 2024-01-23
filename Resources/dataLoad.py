from Resources.item3D import Item3D

# Bele írni első sorként a dimenzió számot, és a szerint megcsinálni a beolvasást

items = []

def fileRead(fileName):
    print(fileName)
    f = open(f"{fileName}", "r")
    lines = f.readlines()
    # print(lines)
    for line in lines:
        x = line.replace('\n', " ").strip().split()
        if len(x) == 3:
            # print(x)
            binSize = [int(x[0]), int(x[1]), int(x[2])]

        if len(x) == 4:
            item = Item3D(int(x[0]), int(x[1]), int(x[2]), int(x[3]))
            items.append(item)

    f.close()
    return items, binSize