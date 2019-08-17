import sys
sys.path.append('/home/daniel/Repos/Computational_Prob_Inference')
from common import comp_prob_inference
from common.comp_prob_inference import plt
from common.comp_prob_inference import np


def simulate():
    # Function returns heads or tails by random
    comp_prob_inference.flip_fair_coin()

    # A list of 100 elements corresponding to heads or tails
    flips = comp_prob_inference.flip_fair_coins(100)

    # Plot the distribution of the heads and tails instances
    comp_prob_inference.plot_discrete_histogram(flips)

    # Plot the frequency of the instances
    comp_prob_inference.plot_discrete_histogram(flips, frequency=True)


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
        coin_side = comp_prob_inference.flip_fair_coin()
        if coin_side == "heads":
            instance += 1

        head_instances.append(instance/(flips + 1))

    plt.ylabel("Flip iteration")
    plt.xlabel("Fraction of heads")
    plt.plot(np.linspace(1, number_of_flips, number_of_flips), head_instances)
    plt.show()


if __name__ == '__main__':
    evaluate_head_instances(10000)
