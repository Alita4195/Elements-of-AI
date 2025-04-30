import random
def main():
    cat_prob = 0.20
    dog_prob = 0.80

    if random.random() < cat_prob: #draw a randome number between 0 and 1
        print("cat")
    else:
        print("dog") 

main()