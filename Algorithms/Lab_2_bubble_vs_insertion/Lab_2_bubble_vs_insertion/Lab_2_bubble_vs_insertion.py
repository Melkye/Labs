import numpy as np
import random
from plot_data import plot_data
def generate_data(n, gen_typ="random"):
    if gen_type=="best":
        a = [i+1 for i in range(n)]
        return a
    elif gen_type=="worst":
        a = [i+1 for i in reversed(range(n))]
        return a
    else:
        a = [i+1 for i in range(n)]
        random.shuffle(a)
        return a

