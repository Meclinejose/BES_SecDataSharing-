import random
import numpy as np
from  Main import  Fitness

def Algm(data,enc_data,key):

    # update the particle position based off new velocity updates
    def update_position():
        for i in range(0, num_dimensions):
            position_i[i] = position_i[i] + velocity_i[i]

    # update new particle velocity
    def update_velocity(pos_best_g):
        w = 0.5  # constant inertia weight (how much to weigh the previous velocity)
        c1 = 1  # cognative constant
        c2 = 2  # social constant

        for i in range (num_dimensions):
            r1, r2 = random.random(), random.random()
            vel_cognitive = c1 * r1 * (pos_best_i[i] - position_i[i])
            vel_social = c2 * r2 * (pos_best_g[i] - position_i[i])
            velocity_i[i] = w * velocity_i[i] + vel_cognitive + vel_social

    # evaluate current fitness
    def evaluate(soln):
        Fit = 0
        for i in range(len(soln)):
            Fit = Fit + soln[i]
        return Fit

    num_dimensions=10       ########################### col size
    err_best_g=-1                   # best error for group
    pos_best_g=[]                   # best position for group
    position_i = []  # particle position
    velocity_i = []  # particle velocity
    pos_best_i = []  # best position individual
    err_best_i = -1  # best error individual
    err_i = -1  # error individual

    for i in range(0, num_dimensions):
        velocity_i.append(random.uniform(-1, 1))
        position_i.append(random.random())

    # check to see if the current position is an individual best
    if err_i < err_best_i or err_best_i == -1:
        pos_best_i = position_i.copy()
        err_best_i = err_i

    # establish the swarm
    swarm=[]
    for i in range(0,10):
        tem = []
        for j in range (num_dimensions):
            tem.append(random.random())
        swarm.append(tem)

    # begin optimization loop
    Solutions = []
    i=0
    while i<100:


        privacy, Nv, Fit = Fitness.func(data, enc_data)

        index = np.argmax(Fit)
        #Fitness.append(Fit[index])
        Solutions.append(swarm[0])

        # determine if current particle is the best (globally)
        if err_i < err_best_g or err_best_g == -1:
            pos_best_g = list(position_i)
            err_best_g = float(err_i)

        # cycle through swarm and update velocities and position
        for k in range (10):
            update_velocity(pos_best_g)
            update_position()
        i+=1

        best_index = np.argmax(Fitness)
        best_solution = Solutions[best_index]

    return key, privacy,Nv
