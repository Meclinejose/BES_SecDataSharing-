import random,math
import numpy as np
from Main import Fitness
def Algm(data,Enc_data,key):
    def generate(n, m, l, u):
        data = []
        for i in range(n):
            tem = []
            for j in range(m):
                tem.append(random.uniform(l, u))
            data.append(tem)
        return data

    N, M, lb, ub = 10, 5, 1, 5
    g, max = 0, 100

    soln = generate(N, M, lb, ub)


    def fitness(soln):
        F = []
        for i in range(len(soln)):
            F.append(random.random())
        return F
    gBest, gfit = [], float('inf')

    def mutatedLeader(pb,pw,Xbest,Xworst,X):
        ML=[]
        p=random.uniform(0,1)
        if p <= pb:
            ML.append(Xbest)
        if pb < p <=pb +pw:
            ML.append(Xworst)
        else:
            ML.append(X[0])
        return ML

    def new_Status(f,fml,X,Ml):
        Xnew=[]
        r=random.uniform(0,1)
        I=random.uniform(1,2)
        for i in range(len(Ml)):
            for j in range(len(Ml[i])):
                if fml < f :
                    Xnew.append(X[i][j]+r*(Ml[i][j]-I*X[i][j]))
                else:
                    Xnew.append(X[i][j]+r*(X[i][j]-I*Ml[i][j]))
        return Xnew

    def final_Status(fnew,f,Xnew,X):
        Xi=[]
        if fnew < f:
            Xi.append(Xnew)
        else:
            Xi.append(X)
        return Xi

    while g<max:
        privacy, Nv, fit = Fitness.func(data, Enc_data)
        #fit = fitness(soln)
        bst = np.argmax(fit)
        worst= np.argmin(fit)
        Xfit, XBest = fit[0], soln[0]   # current best fit, solution
        Xfit, Xworst = fit[0], soln[0]   # current best fit, solution

        ML=mutatedLeader(bst,worst,XBest,Xworst,soln)
        fml=fitness(ML)
        Xnew=new_Status(fit,fml,soln,ML) #New Status
        Fnew=fitness(Xnew)
        Best_Soln=final_Status(Fnew,fit,Xnew,soln)


        g+=1

    return key,privacy,Nv

