import numpy as np

w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                              [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
                   [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])
x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])


def hidden_activation(z):
    return np.maximum(0, z) # ReLU (Rectified Linear Unit) activation function

def output_activation(z):
    # identity (linear) activation. fix this!
    return z

x_test = [[72, 2, 25, 3, 450], [60, 3, 15, 1, 300], [74, 5, 10, 2, 100]]
for item in x_test:
    h1_in = np.dot(item, w0)+b0 # this calculates the linear combination of inputs and weights. it is missing the bias term, fix it!
    h1_out = hidden_activation(h1_in) # apply activation function
    
    h2_in = np.dot(h1_out, w1)+b1 # the output of the previous layer is the input for this layer. it is missing the bias term, fix it!
    h2_out = hidden_activation(h2_in)
    
    out_in = np.dot(h2_out, w2)+b2
    out = output_activation(out_in)
    print(out)