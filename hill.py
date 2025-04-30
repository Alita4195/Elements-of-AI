import math
import random             	# just for generating random mountains                                 	 

# generate random mountains                                                                               	 
w = [random.random()/3, random.random()/3, random.random()/3]
# print(w)
h = [1.+math.sin(1+x/6.)*w[0]+math.sin(-.3+x/9.)*w[1]+math.sin(-.2+x/30.)*w[2] for x in range(100)]
# print(h)
h[0] = 0.0; h[99] = 0.0

def climb(x, h):
    # keep climbing until we've found a summit
    summit = False


    # edit here
    while not summit: #while True. 
        if h[x + 1] > h[x] and h[x + 1] >= h[x - 1]: 
            x = x + 1 # right is higher, go there
        elif h[x - 1] > h[x]:
            x-=1   #left is higher, go there      
        else:
            summit = True
    return x


def main(h):

    # start at a random place                                                                                  	 
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    print("Venla started at %d and got to %d" % (x0, x))
    return x0, x

main(h)