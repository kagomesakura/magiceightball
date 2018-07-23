#magic_eight_ball
import random
answers = input('Ask Me A Question\n:')
eight_ball = [ "Yes! Always!", "It Is So", "Without A Doubt", "Yes, Definitely",
               "No", "Never", "Don't Count On It", ]
print(random.choice(eight_ball))
