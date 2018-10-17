# -*- coding: utf-8 -*-
import random

def generate_random_list(length, rng=(1, 100), typ=int):
    """Return a list that does not necessarily contain any major element."""
    return [typ(random.randint(rng[0], rng[1])) for i in range(length)]

def generate_maj_list(length, major_value=3, rng=(1, 100), typ=int, m="auto"):
    """length: length of the list
    major_value: value of the major element
    rng: range of the values into the list
    typ: type of the values into the list
    m: number of times the major element appears. (if a float is given, then
        number(n) = int(m*n))
    """
    A = []
    major_value = typ(major_value)
    if m is "auto":
        m = length / 2 + 1
    elif isinstance(m, float):
        m = m * length
    m = int(m)
    for i in range(m):
        A.append(major_value)
    for i in range(length-m):
        A.append(typ(random.randint(rng[0], rng[1])))
    random.shuffle(A)
    return A

def naive_major(A):
    m = len(A) // 2 # '//' veut dire 'division entiere'.
    for el in A:
        if A.count(el) > m:
            return el
    return None

def is_major(A, el):
    #pass #...
    # inspiration de l'algorithme du cours
    count=0
    n=len(A)
    for a in A:
        if a == el:
            count += 1
            if count > n/2: break
    else :
        return 0    # si el n'est pas maj
    return 1        # si el est maj

def reduce_list(A):
    #pass #...
    ######################
    # le mode pair:
    #if len(A) % 2 == 0:
    ite = 0; #pour recuperer le nombre d'iteration ex 1.3
    # boucler tant que notre liste n'est pas la plus simple possible
    while len(A) > 1:
        ite += 1
        Aprime = A
        A = []
        i = 0
        while i <= len(Aprime)-2:
            if Aprime[i] == Aprime[i+1]:
                A.append(Aprime[i])
            i += 2
    # debug :
    # print("reduce", A)
    print("nombre d'itération de reduce : ", ite)
    return A

    ######################
    # le mode impair est incorrecte même avec les 2 approches (cf cours)
    # if len(A) % 2 == 1:
    #     pass


def get_major(A):
    #pass # ...
    # si longeur de la liste est 1, alors l'element est forcement maj:
    if len(A) == 1:
        return A[0]
    # si longeur de la liste est pair, on applique la reduction pour avoir
    # une liste simple et on fait "sinon"
    elif len(A) % 2 == 0:
        A = reduce_list(A)
    # sinon on calcul l'element maj avec l'algorithme 9 du cours
    for el in A:
        # debug
        # print("el est :", el)
        # print("A est :", A)
        if is_major(A, el) == 1 :
            return el
        el+=1
    return None



## Zone pour les affichages :

# A = generate_maj_list(length=20, major_value=7)
# #A = generate_maj_list(length=21, major_value=7)
# # print("Exemple de liste avec '7' majoritaire: ", A)
#
# #A = generate_random_list(length=10)
# print("Pour la liste A : ", A)
# print("nous avons l'élément majoritaire : ", get_major(A))
