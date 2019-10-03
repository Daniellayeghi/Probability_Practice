import sys

from coin_flip import core
from coin_flip.core import plt
from coin_flip.core import np


def simulate():
    # Function returns heads or tails by random
    core.flip_fair_coin()

    # A list of 100 elements corresponding to heads or tails
    flips = core.flip_fair_coins(100)

    # Plot the distribution of the heads and tails instances
    core.plot_discrete_histogram(flips)

    # Plot the frequency of the instances
    core.plot_discrete_histogram(flips, frequency=True)


def evaluate_head_instances(number_of_flips: int):
    """
    Function aims to show the convergence of coin flip probability to 0.5

    Input
    -----
    - number_of_flips: the number of flips used to evaluate the convergence

    Output
    ------
    fraction of the heads over the number_of_flips
    """
    head_instances = []
    instance = 0
    for flips in range(number_of_flips):
        coin_side = core.flip_fair_coin()
        if coin_side == "heads":
            instance += 1

        head_instances.append(instance/(flips + 1))

    plt.ylabel("Flip iteration")
    plt.xlabel("Fraction of heads")
    plt.plot(np.linspace(1, number_of_flips, number_of_flips), head_instances)
    plt.show()


def pair_coin_flip_interaction(states: list, number_of_coin_toss: int = 100, number_of_coins: int = 2):
    """
    Function aims to show the joint probability of multiple coins

    Input
    -----
    - states: acceptable states either of the coins could be in
    - number_of_coin_toss: number of tosses used to evaluate probability
    - number of coins: coin sample size

    Output
    ------
    joint probability of the N coins
    """

    if number_of_coins != len(states):
        raise ValueError("Each coin should have an associative state!")

    coin_states = [[] for _ in range(number_of_coins)]
    coin_acc_state = [0 for _ in range(len(states))]

    for coin in range(number_of_coins):
        coin_states[coin] = core.flip_fair_coins(number_of_coin_toss)
        for state in coin_states[coin]:
            if state == states[coin]:
                coin_acc_state[coin] += 1

    final_prob = sum(coin_acc_state)

    coin_equality = [True for _ in range(number_of_coins)]
    for iteration in range(number_of_coin_toss):
        for coin in range(number_of_coins):
            coin_equality[coin] = coin_states[coin][iteration] == states[coin]

        if all(coin_equalities for coin_equalities in coin_equality):
            final_prob -= 1

    return final_prob / number_of_coin_toss


if __name__ == '__main__':
    """
    Testing evaluate_head_instances
    """
    evaluate_head_instances(1000)

    """
    Testing pair_coin_flip_interaction
    """
    number_of_coins = 2
    specified_states = ["heads", "tails"]
    probability = pair_coin_flip_interaction(specified_states, 100000, number_of_coins)
    print("Joint probability of the {0} coins in the specified state is {1}".format(number_of_coins, probability))


