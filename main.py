import random
from math import exp, pi, sqrt, ceil, log10, log
import matplotlib.pylab as plt



def standart_method(r, param):
    return param * sqrt(-2 * log(r))

def fun_standart_method(x, param):
    return 1 - exp(-pow(x,2)/ (2 * pow(param, 2)))
    #return x / pow(param, 2) * exp( - pow(x, 2) / (2 * pow(param, 2)))
def disper(list_elements, mat_ojidanie):
    result = 0
    for i in list_elements:
        result += pow(i - mat_ojidanie, 2)
    result =  result/(N - 1)
    return result

def start(N, param):
    print()
def teor_params(param):
    Mx = sqrt(2 * pi) / 2 * param
    Dx = (4 - pi) / 2 * pow(param, 2)
    print("Теоретическое мат ожидание ", Mx)
    print("Теоретическая дисперсия ", Dx)

def get_randon_numbers_standart_medthod(N):
    list_elements = []
    sum = 0
    for i in range(N):
        r = random.random()
        get_num = standart_method(r, param)
        list_elements.append(get_num)
        sum += get_num

    xmax = max(list_elements)
    xmin = min(list_elements)
    h = (xmax - xmin) / count_segemnts
    gp = h
    rad = {}

    for i in range(count_segemnts):
        rad.update([(i + 1, 0)])
    list_sorted_elements = sorted(list_elements)
    print("Отсортированый массив", list_sorted_elements)
    k = 1
    number = 0
    for i in list_sorted_elements:
        if i < gp:
            k += 1
        else:
            number += 1
            gp += h
            rad.update([(number, k)])
            k = 1
    print(rad)
    result= 0
    gp = h
    for i in rad:
        ideal = N * (fun_standart_method(gp, param) - fun_standart_method(gp - h, param))
        gp += h
        print("Идеальное для ", i ,"-ого ",  ideal)
        result += pow(rad[i] - ideal, 2) / ideal
    print("Кол-во степеней свободы : ", len(rad))
    print("Хи квадрат : ", result)
    print("Мат ожидание фактическое " + str(sum / N))
    print("Дисперсия фактическая " + str(disper(list_sorted_elements, sum / N)))

N = 100
param =0.5#параметр масштаба
count_segemnts = ceil(1 + 3.22 * log10(N))  # кол-во отрезков

get_randon_numbers_standart_medthod(N)
teor_params(param)
