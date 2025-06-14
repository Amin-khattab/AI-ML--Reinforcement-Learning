import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import random 
import math

dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

persons = 10000
col = 10
Selectors = [0] * col
Rewards = [0] * col
ads = []


for n in range(0,persons):
    ad = 0
    max_upper_bound = 0
    for i in range(0,col):
        if Selectors[i] > 0:
            avg_rewards = Rewards[i] / Selectors[i]
            i_delta = math.sqrt(3/2 * math.log(n+1)/Selectors[i])
            upper_bound = avg_rewards+i_delta

        else:
            upper_bound = 1e400
        
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i

    ads.append(ad)
    Selectors[ad] = Selectors[ad] + 1
    amin = dataset.values[n,ad]
    Rewards[ad] = Rewards[ad] + amin

plt.hist(ads)
plt.title("the best ad out of the 10")
plt.xlabel("ads")
plt.ylabel("number of clicks on each ad")
plt.show()


