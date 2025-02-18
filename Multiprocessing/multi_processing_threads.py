# -*- coding: utf-8 -*-
import multiprocessing

def gija1():
    for i in range(100000):
        if i % 10000 == 0:
            print("gija 1: ", i)

def gija2():
    for i in range(100000):
        if i % 10000 == 0:
            print("gija 2: ", i)

def gija3():
    for i in range(100000):
        if i % 10000 == 0:
            print("gija 3: ", i)

if __name__ == "__main__":
    processes = []
    
    x1 = multiprocessing.Process(target=gija1)
    x2 = multiprocessing.Process(target=gija2)
    x3 = multiprocessing.Process(target=gija3)
    
    processes.append(x1)
    processes.append(x2)
    processes.append(x3)
    
    for p in processes:
        p.start()
    
    for p in processes:
        p.join()
    
