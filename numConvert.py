def enter_input():
    nbrs = ["0", '1', '2', '3', '4', '5', "6", "7", "8", "9", "A", "B", "C", "D","E", "F", ".", "-"]
    def verif(l):
        l = str(nbr).upper()
        list_nb = [char for char in l]
        for n in list_nb:
            if n not in nbrs:
                return False
        return True
    nbr = "*"
    while not verif(nbr):
        nbr = input("Entrer le numero : ")
    return nbr

def enter_base(v):
    b = 0
    bases = [str(v) for v in range(2,17,1)]
    while (b not in bases):
        print("============\nLes base sont", bases)
        b = input("Entrer la base {}: ".format(v))
    return b

def verifBase(nbr, base):
    nbrs = ["0", '1', '2', '3', '4', '5', "6", "7", "8", "9", "A", "B", "C", "D", "F", ".", "-"]
    nb = nbr.split(".")
    for nth in nb:
        for n in nth:
            if n.upper() not in nbrs[0:base-1] and n != "-":
                return False
    return True

def to_dec(nbr, b1):
    nbrs = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "-":""}
    nor = ["0", '1', '2', '3', '4', '5', "6", "7", "8", "9"]
    nb = nbr.split('.')
    list_nb = []
    for i, nth in enumerate(nb) :
        list_nb.append([int(v) if v in nor and v != "-" else nbrs[v.upper()] for v in nth])
    res = []
    for j, x in enumerate(list_nb):
        dec = 0
        for i, n in enumerate(x):
            if n != "":
                dec += n * pow(int(b1), len(x)-i-1)
        res.append(str(dec))
    return ".".join(res) if nbr[0] != "-" else "-"+".".join(res)

def to_b2(res, dec1, b21):
    def reVal(num):

        if (num >= 0 and num <= 9):
            return chr(num + ord('0'));
        else:
            return chr(num - 10 + ord('A'));
    dec = int(dec1)
    b2 = int(b21)
    while (dec > 0):
        res += reVal(dec % b2)
        dec = int(dec / b2)
    res = res[::-1]
    return res

def convert():
    num = enter_input()
    b1 = enter_base("de debut")
    b2 = enter_base("de conversion")
    toDec = to_dec(num, b1)
    isSign = True
    if toDec[0] == "-":
        isSign = False
        toDec = toDec[1:]
    nb = toDec.split('.')
    res = []
    for x in nb:
        res.append(to_b2("", x, b2))
    res[1] = [v for v in res[1]]
    if len(res[1])<5:
        for i in range(5-len(res[1])):
            res[1].insert(0, "0")
    aux = res[1][0:5]
    res[1] = ''
    for x in aux:
        res[1] += x
    return '.'.join(res) if isSign else "-"+'.'.join(res)