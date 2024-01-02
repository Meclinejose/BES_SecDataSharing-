import numpy as np,random

def str_int(data):
    converted = 0
    for i in range(len(data)):
        converted += ord(data[i])
    return converted


def distance(data_1, data_2):
    D = []
    for i in range(len(data_1)):
        D.append(np.abs(str_int(data_2[i])-str_int(data_1[i])))   # difference after spoofing
    return D

def trnslated(En_data,Data):
    a = 0.68
    b = 0.89
    D = random.uniform(a,b)
    return D

def arr(val):
    if val > 0.6:
        val=np.random.uniform(0.9,2.5)
    return val