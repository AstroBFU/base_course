'''
Создайте три одномерных массива длины N и заполните их произвольными целыми 
числами в диапазоне от 0 до 100. Найдите наибольший элемент среди всех трех 
массивов. Определите сумму всех элементов созданных массивов.
'''
from random import randint as rndm
N = int(input())
massivs = [[],[],[]]
l = [x for x in range(0,101)]
for cur_m in range(3):
    for i in range(N):
        massivs[cur_m].append(l[rndm(0,100)])
normis = []
for cm in range(3):
    for ci in range(len(massivs[cm])):
        normis.append(massivs[cm][ci])
print(max(normis),sum(normis))