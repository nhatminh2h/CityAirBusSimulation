import time
import numpy as np
import matplotlib.pyplot as plt
import math

def rand_time_gen():
    mu, sigma = 12, 3
    start_time = np.random.normal(mu, sigma, 1000)
    return start_time
    
print(rand_time_gen())
