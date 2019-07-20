# This program is a simulation. This program is also a work in progress.

# You have 'n' fair coins and flip them all at the same. Any that come up tails
# you set aside. The ones that come up heads you flip again. How many rounds do you
# expect to play before only one coin remains


def coin_flip_simulation(number_of_trials, number_of_coins):
    import numpy as np
    import random

    # static_number_of_trials keeps the number of trials entered by the user static.
    # this is used to compute the average number of times it takes to obtain at least one head
    # in the final line of this method.

    static_number_of_trials = number_of_trials

    # counter list will keep the number of rolls per each trial in the list.
    counter_list = []

    while number_of_trials > 0:
        # 1 represents heads. 0 represents tails
        coins = np.random.randint(2, size=number_of_coins)
        counter = 0

        while sum(coins) > 1:
            for i in range(len(coins)):

                counter = counter + 1
                if coins[i] == 1:
                    coins[i] = random.randint(0, 1)
                if sum(coins) == 1:
                    break
        number_of_trials = number_of_trials - 1

        # This line appends the total number of times it takes a sequence of coin flips to return at least one head.

        counter_list.append(counter)

    # I wanted to return the expected number of times that a head turns up in a sequence of coin flips.
    return (sum(counter_list) / static_number_of_trials)

number_coins = 4

print('This program is a statistical simulation.')
print('The expected number of coin flips you need until one head comes up from flipping ')
print(str(number_coins) + ' coins: ' + str(coin_flip_simulation(5, number_coins)))




