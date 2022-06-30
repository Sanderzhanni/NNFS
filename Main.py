import matplotlib.pyplot as plt
import numpy as np

# output = weight * input + bias

def graph(weight, bias):
    x = np.linspace(-5,5,100)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, weight * x + bias)
    plt.show()


if __name__ == "__main__":

    batch = [[1, 2, 3, 2.5], [2, 5, -1, 2], [-1.5, 2.7, 3.3, -0.8]]
    weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
    biases = [2, 3, 0.5]
    
    outputs = np.dot(np.array(weights).T, batch)
    print(outputs)


    
