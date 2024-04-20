import numpy as np


def generateClasses():
    # itemdb = [5, 25, 50, 100, 200]  # Hány darab tárgy legyen egy példában, az eddig legenárlatakat megtartom csak létrehozok még nagyobbakat is
    itemdb = [400, 800, 1000]

    for i in itemdb:
        dataCorrelated(i)
        """
        # Class1: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 100 és 400 között van
        dataClass("class1", 1000, 1000, 1000, i, 100, 400, 100, 400, 100, 400)
        # Class2: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 1 és 1000 között van
        dataClass("class2", 1000, 1000, 1000, i, 1, 1000, 1, 1000, 1, 1000)
        # Class3: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 200 és 800 között van
        dataClass("class3", 1000, 1000, 1000, i, 200, 800, 200, 800, 200, 800)
        # Class4: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 50 és 200 között van
        dataClass("class4", 1000, 1000, 1000, i, 50, 200, 50, 200, 50, 200)
        # Class5: Ládák mindegyik dimenziója 1000 és a tárgyak mindegyik dimenzióbeli méretei 25 és 100 között van
        dataClass("class5", 1000, 1000, 1000, i, 25, 100, 25, 100, 25, 100)
        # a Class4 és 5 esetén az 5 darabosnak nem lesz sok haszna emrt mindig bele dog férni egy ládába, de a többinél jó tesztesetek lehetnek manuális ellenőrzésre

        # Class6: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [1,1/2*LádaMéret][2/3*LádaMéret,LádaMéret][2/3*LádaMéret,LádaMéret]
        # dataClass("class6", 100, 100, 100, i, 1, 50, 66, 100, 66, 100)
        # Class7: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [2/3*LádaMéret,LádaMéret][1,1/2*LádaMéret][2/3*LádaMéret,LádaMéret]
        # dataClass("class7", 100, 100, 100, i, 66, 100, 1, 50, 66, 100)
        # Class8: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [2/3*LádaMéret,LádaMéret][2/3*LádaMéret,LádaMéret][1,1/2*LádaMéret]
        # dataClass("class8", 100, 100, 100, i, 66, 100, 66, 100, 1, 50)
        # Class9: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [1/2*LádaMéret,100][1/2*LádaMéret,LádaMéret][1/2*LádaMéret,LádaMéret]
        # dataClass("class9", 100, 100, 100, i, 50, 100, 50, 100, 50, 100)
        # Class10: Ládák mindegyik dimenziója 100 és a tárgyak dimenziói rendre [1,1/2*LádaMéret][1,1/2*LádaMéret][1,1/2*LádaMéret]
        dataClass("class6", 100, 100, 100, i, 1, 50, 1, 50, 1, 50)

        # Class11: Ládák mindegyik dimenziója 10 és a tárgyak mindegyik dimenzióbeli méretei 1 és 10 között van
        dataClass("class7", 10, 10, 10, i, 1, 10, 1, 10, 1, 10)
        # Class12: Ládák mindegyik dimenziója 40 és a tárgyak mindegyik dimenzióbeli méretei 1 és 35 között van
        dataClass("class8", 40, 40, 40, i, 1, 35, 1, 35, 1, 35)
        
        dataClass4d("class1", 1000, 1000, 1000, 1000, i, 100, 400, 100, 400, 100, 400, 100, 400)
        dataClass4d("class2", 1000, 1000, 1000, 1000, i, 1, 1000, 1, 1000, 1, 1000, 1, 1000)
        dataClass4d("class3", 1000, 1000, 1000, 1000, i, 200, 800, 200, 800, 200, 800, 200, 800)
        dataClass4d("class4", 1000, 1000, 1000, 1000, i, 50, 200, 50, 200, 50, 200, 50, 200)
        dataClass4d("class5", 1000, 1000, 1000, 1000, i, 25, 100, 25, 100, 25, 100, 25, 100)
        dataClass4d("class6", 100, 100, 100, 100, i, 1, 50, 1, 50, 1, 50, 1, 50)
        dataClass4d("class7", 10, 10, 10, 10, i, 1, 10, 1, 10, 1, 10, 1, 10)
        dataClass4d("class8", 40, 40, 40, 40, i, 1, 35, 1, 35, 1, 35, 1, 35)

        dataClass6d("class1", 1000, 1000, 1000, 1000, 1000, 1000, i, 100, 400, 100, 400, 100, 400, 100, 400, 100, 400, 100, 400)
        dataClass6d("class2", 1000, 1000, 1000, 1000, 1000, 1000, i, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000, 1, 1000)
        dataClass6d("class3", 1000, 1000, 1000, 1000, 1000, 1000, i, 200, 800, 200, 800, 200, 800, 200, 800, 200, 800, 200, 800)
        dataClass6d("class4", 1000, 1000, 1000, 1000, 1000, 1000, i, 50, 200, 50, 200, 50, 200, 50, 200, 50, 200, 50, 200)
        dataClass6d("class5", 1000, 1000, 1000, 1000, 1000, 1000, i, 25, 100, 25, 100, 25, 100, 25, 100, 25, 100, 25, 100)
        dataClass6d("class6", 100, 100, 100, 100, 100, 100, i, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50, 1, 50)
        dataClass6d("class7", 10, 10, 10, 10, 10, 10, i, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10, 1, 10)
        dataClass6d("class8", 40, 40, 40, 40, 40, 40, i, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35, 1, 35)
        """

def dataClass(className, b1, b2, b3, i, ws, wl, hs, hl, ds, dl):
    # láda dimenzióinak maximális kapacitása
    b1 = b1
    b2 = b2
    b3 = b3

    r = open("C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/3D_Classes/FileNames3.txt", "a")
    r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/3D_Classes/{className}_{i}_3.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/3D_Classes/{className}_{i}_3.txt", "w")
    f.write(str(i) + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + " \n")
    for x in range(i):
        w = np.random.random_integers(ws, wl)
        h = np.random.random_integers(hs, hl)
        d = np.random.random_integers(ds, dl)

        f.write(str(x + 1) + " " + str(w) + " " + str(h) + " " + str(d) + " \n")
    r.close()
    f.close()


def dataClass4d(className, b1, b2, b3, b4, i, s1, l1, s2, l2, s3, l3, s4, l4):
    # láda dimenzióinak maximális kapacitása
    b1 = b1
    b2 = b2
    b3 = b3
    b4 = b4

    r = open("C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/FileNames.txt", "a")
    r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/{className}_{i}_3.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/{className}_{i}_3.txt", "w")
    f.write("4" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + str(b4) + " " + " \n")
    for x in range(i):
        d1 = np.random.random_integers(s1, l1)
        d2 = np.random.random_integers(s2, l2)
        d3 = np.random.random_integers(s3, l3)
        d4 = np.random.random_integers(s4, l4)

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " " + str(d3) + " " + str(d4) + " \n")
    r.close()
    f.close()


def dataClass6d(className, b1, b2, b3, b4, b5, b6, i, s1, l1, s2, l2, s3, l3, s4, l4, s5, l5, s6, l6):
    # láda dimenzióinak maximális kapacitása
    b1 = b1
    b2 = b2
    b3 = b3
    b4 = b4
    b5 = b5
    b6 = b6

    r = open("C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/FileNames.txt", "a")
    r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/{className}_{i}_3.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/{className}_{i}_3.txt", "w")
    f.write("6" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + str(b4) + " " + str(b5) + " " + str(b6) + " \n")
    for x in range(i):
        d1 = np.random.random_integers(s1, l1)
        d2 = np.random.random_integers(s2, l2)
        d3 = np.random.random_integers(s3, l3)
        d4 = np.random.random_integers(s4, l4)
        d5 = np.random.random_integers(s5, l5)
        d6 = np.random.random_integers(s6, l6)

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " " + str(d3) + " " + str(d4) + " " + str(d5) + " " + str(d6) + " \n")
    r.close()
    f.close()


def dataCorrelated(i):
    # láda dimenzióinak maximális kapacitása
    b1 = 150
    b2 = 150
    b3 = 150
    b4 = 150
    b5 = 150
    b6 = 150
    """
    # r = open("C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/2D_Classes/FileNames.txt", "a")
    # r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/2D_Classes/class9.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/2D_Classes/class9_{i}.txt", "w")
    f.write("2" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + " \n")
    for x in range(i):
        d1 = np.random.random_integers(20, 100)
        d2_s = np.random.random_integers(0, 10)
        d2_p = np.random.random_integers(0, 1)

        if d2_p:
            d2 = d1 + d2_s
        else:
            d2 = d1 - d2_s

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " \n")
    f.close()

    # r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/2D_Classes/class10.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/2D_Classes/class10_{i}.txt", "w")
    f.write("2" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + " \n")
    for x in range(i):
        d1 = np.random.random_integers(20, 100)
        d2_s = np.random.random_integers(110, 130)

        d2 = d2_s - d1

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " \n")
    # r.close()
    f.close()
    """
    #  r = open("C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/FileNames.txt", "a")
    #  r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/class9.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/class9_{i}.txt", "w")
    f.write("4" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + str(b4) + " " + " \n")
    for x in range(i):
        d1 = np.random.random_integers(20, 100)
        d2_s = np.random.random_integers(0, 10)
        d2_p = np.random.random_integers(0, 1)

        if d2_p:
            d2 = d1 + d2_s
        else:
            d2 = d1 - d2_s

        d3 = np.random.random_integers(20, 100)
        d4_s = np.random.random_integers(0, 10)
        d4_p = np.random.random_integers(0, 1)

        if d4_p:
            d4 = d3 + d4_s
        else:
            d4 = d3 - d4_s

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " " + str(d3) + " " + str(d4) + " \n")
    f.close()

    #  r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/class10.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/4D_Classes/class10_{i}.txt", "w")
    f.write("4" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + str(b4) + " " + " \n")
    for x in range(i):
        d1 = np.random.random_integers(20, 100)
        d2_s = np.random.random_integers(110, 130)

        d2 = d2_s - d1

        d3 = np.random.random_integers(20, 100)
        d4_s = np.random.random_integers(110, 130)

        d4 = d4_s - d3

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " " + str(d3) + " " + str(d4) + " \n")
    # r.close()
    f.close()

    #  r = open("C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/FileNames.txt", "a")
    # r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/class9.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/class9_{i}.txt", "w")
    f.write("6" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + str(b4) + " " + str(b5) + " " + str(b6) + " \n")
    for x in range(i):
        d1 = np.random.random_integers(20, 100)
        d2_s = np.random.random_integers(0, 10)
        d2_p = np.random.random_integers(0, 1)

        if d2_p:
            d2 = d1 + d2_s
        else:
            d2 = d1 - d2_s

        d3 = np.random.random_integers(20, 100)
        d4_s = np.random.random_integers(0, 10)
        d4_p = np.random.random_integers(0, 1)

        if d4_p:
            d4 = d3 + d4_s
        else:
            d4 = d3 - d4_s

        d5 = np.random.random_integers(20, 100)
        d6_s = np.random.random_integers(0, 10)
        d6_p = np.random.random_integers(0, 1)

        if d6_p:
            d6 = d5 + d6_s
        else:
            d6 = d5 - d6_s

        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " " + str(d3) + " " + str(d4) + " " + str(d5) + " " + str(d6) + " \n")
    f.close()

    # r.write(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/class10.txt\n")

    f = open(f"C:/Users/koloz/PycharmProjects/Pakolas_tdk/Data/6D_Classes/class10_{i}.txt", "w")
    f.write("6" + " \n")
    f.write(str(b1) + " " + str(b2) + " " + str(b3) + " " + str(b4) + " " + str(b5) + " " + str(b6) + " \n")
    for x in range(i):
        d1 = np.random.random_integers(20, 100)
        d2_s = np.random.random_integers(110, 130)

        d2 = d2_s - d1

        d3 = np.random.random_integers(20, 100)
        d4_s = np.random.random_integers(110, 130)

        d4 = d4_s - d3

        d5 = np.random.random_integers(20, 100)
        d6_s = np.random.random_integers(110, 130)

        d6 = d6_s - d5
        f.write(str(x + 1) + " " + str(d1) + " " + str(d2) + " " + str(d3) + " " + str(d4) + " " + str(d5) + " " + str(d6) + " \n")
    # r.close()
    f.close()
