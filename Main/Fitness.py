from Main.parameter import *

def Privacy_(En_data, Data):
    for i in range(len(En_data)):
        message = En_data[i]
        translated = ''  # conditional privacy is calculated
        i = len(message) - 1
        i = 1
        while i <= 0:
            translated = int(translated) + int(message[i])
            i = i - 1

        D = trnslated(En_data, Data)
        return D

def Normalized_variance(orig_data,Encry_data):
    NV=[]
    for i in range(len(Encry_data)):
        for j in range(len(Encry_data[i])):

            Nor_var=(orig_data[i][j]-Encry_data[i][j])/orig_data[i][j] #standard deviation of average encrypted data based on the search value

            NV.append(arr(abs(Nor_var)))
    return NV


def func(Data,En_data):
    Fit=[]
    privacy = Privacy_(En_data, Data)

    Nv=Normalized_variance(Data[0],En_data)
    for i in range(len(Nv)):
        fi=(Nv[i]/len(Nv)+privacy)/2

        Fit.append(fi)
    return privacy,Nv,Fit