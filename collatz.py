import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import csv

# DEFINITION OF FUNCTIONS


def collatz_odd(x):
    result = (3 * x) + 1
    return result

def collatz_even(x):
    result = x / 2
    return result

def isEven(x):
    return x % 2 == 0

def stop_check(x):
    return x == 1


x = input('What number do you want to test?\n')
x = int(x)
runUserCode = True

while runUserCode:
    results = []
    results.append(x)
    while stop_check(x) == False:
        if isEven(x) == True:
            x = collatz_even(x)
        elif isEven(x) == False:
            x = collatz_odd(x)
        results.append(x)
    print(f" these are the results: {results}")
    split_lists = [results[x:x+1] for x in range(0, len(results), 1)]
    collatz_df = pd.DataFrame(results)
    collatz_df.columns = ['Path']
    print(collatz_df)
    plt.plot(collatz_df["Path"])
    plt.show()
    runUserCode = False

