'''
Created on Dec 16, 2015

@author: teaddict
'''

import math
import random

machines = [[4,5,3],[8,9,3]]
jobs = [[0,2,4],[5,0,6],[7,8,0]]
delimiter = -1

def anneal(sol):
    old_cost = cost(sol)
    best_cost = old_cost
    T = 1.0
    T_min = 0.00001
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 100:
            new_sol = neighbor(sol)
            new_cost = cost(new_sol)
            if(new_cost<best_cost):
                best_cost = new_cost
            ap = acceptance_probability(old_cost, new_cost, T)
            if ap > random_probability():
                sol = new_sol   
                old_cost = new_cost
            i += 1
        T = T*alpha
    return sol, best_cost


def random_job():
    randomJob=random.sample(range(0,3), 4)
    i=0
    while i<len(randomJob):
        if randomJob[i]==3:
            randomJob[i]=-1
            break
    return randomJob

def random_probability():
    return  float(random.randint(0,1000)) / 1000

def cost(sol):
    i=0
    time=0
    last = sol[i]
    second_machine_first_run = True
    while i<len(sol):
        if(sol[i]==-1):
            if i+1<len(sol):
                i+=1
                time += machines[1][sol[i]]
                last = sol[i]
                i+=1
            while(i<len(sol)):
                time += machines[1][sol[i]]
                time += jobs[last][sol[i]]
                last = sol[i]
                i+=1
        else:
            print(sol[i])
            time += machines[0][sol[i]]
            time += jobs[last][sol[i]]
            last = sol[i]
        i+=1
    return time

def neighbor(sol):
    j = random.sample(range(0,3), 1)
    i = j[0]
    temp=sol[i]
    sol[i]=sol[i+1]
    sol[i+1]=temp
    return sol

def acceptance_probability(old_cost, new_cost, T):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp(-(new_cost - old_cost) / T)

def main():
    sol = [-1, 0, 2, 1]
    print(anneal(sol))

main()