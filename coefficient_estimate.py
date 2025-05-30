import numpy as np

def main():
    np.set_printoptions(precision=1)

    x = np.array([
                [25, 2, 50, 1, 500], 
                [39, 3, 10, 1, 1000], 
                [13, 2, 13, 1, 1000], 
                [82, 5, 20, 2, 120], 
                [130, 6, 10, 2, 600],
                [115, 6, 10, 1, 550]
                ])   
    y = np.array([127900, 222100, 143750, 268000, 460700, 407000])

    c = np.linalg.lstsq(x, y)[0] #return a tuple, without[0]
    print(c) #estimated coefficients
    print(x @ c) #least squares fit
main()