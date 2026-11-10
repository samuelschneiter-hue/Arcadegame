import random
import math
print("Game is loading....")
L=0
def checker(v1, v2):
    if v2 >= v1:
        print("failed at checker")
    elif v1 >= v2:
        print("Level completed successfully")
        nextlvl(L+1)
def nextlvl(C):
    if L == 0:
        print("Erstes Level startet...")

nextlvl(L)
RD=random.randint(1,3)
print(RD)