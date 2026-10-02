import numpy as np
r = np.random.random()
print(r)
rand_nb = np.random.randint(0, 101)
print(rand_nb)

correct = False

while not correct :
    user_guess = int(input("Guess a number between 0 and 100: "))

    if user_guess == rand_nb:
        correct = True
    elif user_guess > rand_nb :
        print("the number to guess is Lower")
    else:
        print("the number to guess is Higher")

print("congratulations! You guessed the number.")

