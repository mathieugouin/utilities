#!/usr/bin/python


from __future__ import print_function
import random

points_jeremie = 0
points_ordi = 0


def print_bravo():
    global points_jeremie
    points_jeremie += 1
    print("Bravo!     {} a {}".format(points_jeremie, points_ordi))


def print_error():
    global points_ordi
    msg = [
    'rig rag',
    'patate',
    'banane',
    'puree de poisson',
    'asperge',
    'petit pois',
    'M. Tout Cru',
    'Mme. Tout Cru',
    'petit pet',
    'puree de rondelle',
    'nom d\'un caca boudin',
    'nom d\'un jackstrap',
    ]
    
    points_ordi += 1
    print("Erreur, Jeremie {}      {} a {}".format(msg[random.randint(0, len(msg) - 1)], points_jeremie, points_ordi))


def input_int():
    x = -99999999
    valid = False
    try:
        x = int(input(""))
        valid = True
    except Exception as e:
        print("Ceci n'est pas un nombre entier")
    return (x, valid)


def mul_quiz():
    x = random.randint(1, 10)
    y = random.randint(1, 12)
    z = x * y
    good = False
    while not good:
        print("{} x {} = ".format(x, y), end="")
        t, v = input_int()
        if v:
            if t != z:
                print_error()
            else:
                good = True
                print_bravo()


def add_quiz():
    x = random.randint(0, 12)
    y = random.randint(0, 12)
    z = x + y
    good = False
    while not good:
        print("{} + {} = ".format(x, y), end="")
        t, v = input_int()
        if v:
            if t != z:
                print_error()
            else:
                good = True
                print_bravo()


def sub_quiz():
    x = random.randint(0, 12)
    y = random.randint(0, min(x, 12))
    z = x - y
    good = False
    while not good:
        print("{} - {} = ".format(x, y), end="")
        t, v = input_int()
        if v:
            if t != z:
                print_error()
            else:
                good = True
                print_bravo()


op_dic = {
    0: add_quiz,
    1: sub_quiz,
    2: mul_quiz,
}

while True:
    op = random.randint(0, len(op_dic) - 1) # [min - max]
    op_dic[op]()
