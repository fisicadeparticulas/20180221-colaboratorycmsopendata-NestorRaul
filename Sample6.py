#!/usr/bin/env python

import matplotlib.pyplot as plt
import math

F = open("Sample6.csv","r")

M = []
L = F.readlines()

for i in range(1,20001):
	L[i] = L[i].split(",")

	M = M + [math.sqrt(2*float(L[i][7])*float(L[i][16])*(math.cosh(float(L[i][8])-float(L[i][17]))-math.cos(float(L[i][9])-float(L[i][18]))))]

plt.title('Masa')
plt.hist(M,200)
plt.grid(True)
plt.savefig("Hist.png")
plt.show()
plt.clf()
