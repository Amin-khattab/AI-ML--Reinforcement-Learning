import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import random

dataset = pd.read_csv("Ads_CTR_Optimisation.csv")


N = 300
col = 10
Number_rewards_1 = [0] * col
Number_rewards_0 = [0] * col
ads = []
for n in range(0,N):
    ad = 0
    max_random = 0
    for i in range(0,col):
        theta = random.betavariate(Number_rewards_1[i]+1 , Number_rewards_0[i]+1)

        if theta > max_random:
            max_random = theta
            ad = i

    rewards = dataset.values[n,ad]

    if rewards == 1:
        Number_rewards_1[ad] = Number_rewards_1[ad] + 1
    else:
        Number_rewards_0[ad] = Number_rewards_0[ad] + 1

    ads.append(ad)

plt.hist(ads)
plt.show()
