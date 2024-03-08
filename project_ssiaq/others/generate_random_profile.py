import numpy as np
import json

"""
Script to generate random profile factors (8760 for hourly values of year) for variation of usage profiles 
in useconditions of TEASER
"""
profile_factor = list()
for i in range(8760):
    rng = np.random.default_rng()
    mu = 0                              # mean value of distribution
    sigma = 0.1                         # standard deviation of distribution (0.1 - initial value)
    sample = 100                        # sample size to draw random number from
    s = rng.normal(mu, sigma, sample)   # draw samples from distribution
    random_value = rng.choice(s)        # select single values from distribution
    profile_factor.append(random_value)

# save to json file
with open("../random_profile_factors.json", 'w') as f:
    json.dump(profile_factor, f, indent=2)

print("Generated and exported profile!")
