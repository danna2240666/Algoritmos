import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter_ns
import random as rnd
from random import random, randrange

def bubble_sort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L
def insertion_sort(L):
    i = 1
    while i < len(L):
        j = i
        while j > 0 and L[j - 1] > L[j]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1
        i += 1
    return L
def partition(L, low, high):
    m = int((low + high) / 2)
    if L[m] < L[low]: 
        L[low], L[m] = L[m], L[low]
    if L[high] < L[low]:
        L[low], L[high] = L[high], L[low]
    if L[m] < L[high]:
        L[m], L[high] = L[high], L[m] 
    pivot = L[high]
    
    i = low - 1
    
    for j in range(low, high):
        if L[j] <= pivot:
            i = i + 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    return i + 1

def quickSort(L, low, high):
    if low < high:
        pi = partition(L, low, high)
        quickSort(L, low, pi - 1)
        quickSort(L, pi + 1, high)
    return L
def selection_sort(L):
    for i in range(len(L) - 1):
        min = i
        for j in range(i + 1, len(L)):
            if (L[min] > L[j]):
                min = j
        if min != i:
            L[min], L[i] = L[i], L[min]
    return L


num_elements = np.arange(1000, 10001, 1000)
size = num_elements.size
print(size)
#print(num_elements)
t_bubble = np.zeros(size)
t_selection = np.zeros(size)
t_insertion = np.zeros(size)
t_quick_sort = np.zeros(size)

for i, n in enumerate(num_elements) :
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    bubble_sort(vector_ord)
    t_final = perf_counter_ns()
    t_bubble[i] = t_final - t_inicio
    
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    insertion_sort(vector_ord)
    t_final = perf_counter_ns()
    t_insertion[i]= t_final - t_inicio
    
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    quickSort(vector_ord, 0, len(vector_ord)-1)
    t_final = perf_counter_ns()
    t_quick_sort[i]= t_final - t_inicio
    
    vector_ord = np.random.randint(0, 100, n, dtype=np.int16)
    t_inicio = perf_counter_ns()
    selection_sort(vector_ord)
    t_final = perf_counter_ns()
    t_selection[i]= t_final - t_inicio

plt.plot(num_elements, t_bubble, "g-")
#plt.show()
plt.plot(num_elements, t_insertion, "y-")
#plt.show()
plt.plot(num_elements, t_quick_sort, "b-")
#plt.show()
plt.plot(num_elements, t_selection, "r-")
plt.show()