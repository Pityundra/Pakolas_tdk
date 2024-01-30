from Resources.Item.item1D import Item1D
from Resources.Item.item2D import Item2D
from Resources.Item.item3D import Item3D


def splitData(fileName):

    f = open(f"Data/3D_Classes/{fileName}.txt", "r")
    lines = f.readlines()
    firstLine = lines[0].replace('\n', " ").strip().split()
    secondLine = lines[1].replace('\n', " ").strip().split()

    w1 = open(f"Data/1D_Classes/{fileName}_1.txt", "w")
    w1.write("1 \n")
    w1.write(secondLine[0] + " " + " \n")

    w2 = open(f"Data/1D_Classes/{fileName}_2.txt", "w")
    w2.write("1 \n")
    w2.write(secondLine[1] + " " + " \n")

    w3 = open(f"Data/1D_Classes/{fileName}_3.txt", "w")
    w3.write("1 \n")
    w3.write(secondLine[2] + " " + " \n")

    w4 = open(f"Data/2D_Classes/{fileName}_1.txt", "w")
    w4.write("2 \n")
    w4.write(secondLine[0] + " " + secondLine[1] + " \n")

    w5 = open(f"Data/2D_Classes/{fileName}_2.txt", "w")
    w5.write("2 \n")
    w5.write(secondLine[0] + " " + secondLine[2] + " \n")

    w6 = open(f"Data/2D_Classes/{fileName}_3.txt", "w")
    w6.write("2 \n")
    w6.write(secondLine[1] + " " + secondLine[2] + " \n")

    lines.pop(0)
    lines.pop(0)

    for line in lines:
        x = line.replace('\n', " ").strip().split()
        w1.write(x[0] + " " + x[1] + " \n")
        w2.write(x[0] + " " + x[2] + " \n")
        w3.write(x[0] + " " + x[3] + " \n")

        w4.write(x[0] + " " + x[1] + " " + x[2] + " \n")
        w5.write(x[0] + " " + x[1] + " " + x[3] + " \n")
        w6.write(x[0] + " " + x[2] + " " + x[3] + " \n")


    f.close()
    w1.close()
    w2.close()
    w3.close()
    w4.close()
    w5.close()
    w6.close()