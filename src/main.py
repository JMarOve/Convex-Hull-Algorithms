import sys


from utils import *
from ch_algos.GrahamScan import *


if __name__ == "__main__":
    data = sample_generator()
    hull = grahamscan(data)
    fig,ax = scatter_plot(data,hull)
    plt.show()