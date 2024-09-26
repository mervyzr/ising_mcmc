import numpy as np
import matplotlib.pyplot as plt

def main(N, itr=1e5, **kwargs):
    states = []
    burn_in = int(.1 * itr)

    try:
        J = float(kwargs["J"])
    except Exception as e:
        J = 1  # anti-ferromagnetic

    try:
        h = float(kwargs["h"])
    except Exception as e:
        h = 1  # magnetic field strength

    try:
        T = float(kwargs["T"])
    except Exception as e:
        T = 1
    finally:
        beta = 1/T

    arr = np.random.randint(0, 2, size=(N,N))
    arr[arr == 0] = -1

    for i in range(int(itr)):
        states.append(arr)
        padded_arr = np.pad(arr, ((1,1),(1,1)), mode="wrap")
        x,y = np.random.choice(np.arange(1, N-1), size=2)
        diff_E = -2*J*-padded_arr[x,y]*(padded_arr[x+1,y] + padded_arr[x-1,y] + padded_arr[x,y+1] + padded_arr[x,y-1]) + 2*padded_arr[x,y]*h

        alpha = np.exp(-beta * diff_E)

        if alpha >= np.random.uniform(0,1):
            padded_arr[x,y] *= -1
            arr = padded_arr[1:-1,1:-1]

    return np.asarray(states[burn_in:])

if __name__ == "__main__":
    states = main(64)
    y = np.sum(states, axis=(1,2))/64**2
    x = np.arange(len(states))
    plt.plot(x,y)
    plt.show()