import numpy as np
import matplotlib.pyplot as plt

def main(itr=1e6, limit=5):

    def dist(x):
        return np.exp(-x**2)/np.sqrt(np.pi)

    values = []
    burn_in = int(.1 * itr)

    value = np.random.randint(-limit,limit)
    for jump in range(int(itr)):
        values.append(value)
        _next = value + np.random.uniform(-1,1)

        ratio = min(dist(_next)/dist(value), 1)

        if ratio >= np.random.uniform(0,1):
            value = _next

    return np.asarray(values[burn_in:])

if __name__ == "__main__":
    main()