import math,random,numpy as np
from math import gamma
from Main import Fitness
def Algm(data,En_da,Key):
    def initialize_soln(N, M):  # solution
        soln = []
        for i in range(N):  # N rows, M columns
            tem = []
            for j in range(M): tem.append(random.random())  # random values
            soln.append(tem)
        return soln

    def fitness(solution): # fitness calculation
        fit = []
        for i in range(len(solution)):
            sum = 0
            for j in range(len(solution[i])):
                sum += solution[i][j] # summation of soln.
            fit.append(sum)
        return fit

    def find_mean(soln):

        Xmean=[]
        for i in range(len(soln)):
            xm=0
            for j in range(len(soln[i])):
                xm+=soln[i][j]
            mean = (1/len(soln))*xm
            Xmean.append(mean)
        return Xmean

    def levy():
        s, u, v, beta = 0.01, random.random(), random.random(), 1.5
        sigma = (gamma(1 + beta) * np.sin(np.pi * beta / 2) / (gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (
                    1 / beta)
        step = s*((u*sigma)  / abs(v) ** (1 / beta))
        return step

    def expanded_exploration(X_best,X_M,t,rand):
        pos_new=[]
        for i in range(len(X_best)):
            tem=[]
            for j in range(len(X_best[i])):
                tem.append(X_best[i][j]*(1-t/Tmax)+(X_M[i]-X_best[i][j]*rand)) # Eq.3
            pos_new.append(tem)
        return pos_new

    def narrowed_exploration(X_best,levy,rand):
        r = random.randint(0,N-1)
        Xr=X_best[r]
        pos_new = []
        for i in range(len(X_best)):
            tem = []
            for j in range(len(X_best[i])):
                tem.append(X_best[i][j] * levy + Xr[i]+(y-x)*rand)  # Eq.5
            pos_new.append(tem)
        return pos_new

    def expanded_exploitation(X_best,X_M,rand):
        pos_new=[]
        for i in range(len(X_best)):
            tem=[]
            for j in range(len(X_best[i])):
                tem.append(((X_best[i][j]*X_M[i])*alpha-rand+((UB-LB)*rand+LB)*delta)) # Eq.13
            pos_new.append(tem)
        return pos_new

    def narrowed_exploitation(X_best,levy,rand,QF):
        pos_new = []
        for i in range(len(X_best)):
            tem = []
            for j in range(len(X_best[i])):
                tem.append(QF*X_best[i][j]-(G1*population[i][j]*rand)-G2*levy+rand*G1)  # Eq.14
            pos_new.append(tem)
        return pos_new



    alpha,delta=0.1,0.1
    N,M=10,10
    t=0
    Tmax=5
    LB,UB=1,Key
    population = initialize_soln(N,M)
    Fit = []
    overall_best = []
    overall_fit = []
    # Main loop
    while (t < Tmax):
        new_solution = []
        privacy, Nv, Fit = Fitness.func(data, En_da)
        #Fit = fitness(population)  # fitness calculation
        best = np.argmax(Fit)  # minimization problem
        overall_fit.append(min(Fit))
        overall_best.append(population[0])

        h = random.random()
        Xm=find_mean(population) # Mean
        G1,G2=2*random.random()-1 , 2*(1-(t/Tmax))
        w,r1,U,D1=0.005,random.uniform(1,20),0.00565,random.randint(1,M)
        s,u,v,beta=0.01,random.random(),random.random(),1.5
        teta1=(3*np.pi)/2
        teta=-w*D1+teta1
        r=r1+U*D1
        x=r*math.sin(teta)
        y=r*math.cos(teta)
        step = levy()
        rand = random.random()
        if(t<=(2/3)*Tmax):
            X_best = population
            if(rand<0.5):
                pos_new=expanded_exploration(X_best,Xm,t,rand)
                new_fit = fitness(pos_new)  # fitness calculation
                if(np.min(new_fit))<(np.min(Fit)):
                    population = pos_new.copy()
                    best = np.argmin(new_fit)  # minimization problem
                    overall_fit.append(min(new_fit))
                    overall_best.append(population[best])
                else:
                    population = pos_new.copy()
            else:
                pos_new = narrowed_exploration(X_best, step,rand)
                new_fit = fitness(pos_new)  # fitness calculation
                if (np.min(new_fit)) < (np.min(Fit)):
                    population = pos_new.copy()
                    best = np.argmin(new_fit)  # minimization problem
                    overall_fit.append(min(new_fit))
                    overall_best.append(population[best])
                else:
                    population = pos_new.copy()
            if (rand < 0.5):
                pos_new = expanded_exploitation(X_best, Xm, rand)
                new_fit = fitness(pos_new)  # fitness calculation
                if (np.min(new_fit)) < (np.min(Fit)):
                    population = pos_new.copy()
                    best = np.argmin(new_fit)  # minimization problem
                    overall_fit.append(min(new_fit))
                    overall_best.append(population[best])
                else:
                    population = pos_new.copy()

            else:
                QF = (t + 1) ** ((2 * np.random.rand() - 1) / (1 - Tmax) ** 2)  # Eq.(15)        Quality function
                pos_new = narrowed_exploitation(X_best, step, rand,QF)
                new_fit = fitness(pos_new)  # fitness calculation
                if (np.min(new_fit)) < (np.min(Fit)):
                    population = pos_new.copy()
                    best = np.argmin(new_fit)  # minimization problem
                    overall_fit.append(min(new_fit))
                    overall_best.append(population[best])
        else:
            population=pos_new.copy()

        t+=1

    return Key,privacy,Nv






