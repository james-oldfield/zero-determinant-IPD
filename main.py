import numpy as np
from argparse import ArgumentParser

parser = ArgumentParser(description='')
parser.add_argument('--debug', required=False)
args = parser.parse_args()

debug = args.debug

# Define the standard short-term payoff vectors for a PD
default_payoffs = {
    'X': np.array([[5, 3, 1, 0]]),
    'Y': np.array([[5, 1, 3, 0]]),
}


def compute_equilibrium_payoffs(S_x=default_payoffs.get('X'),
                                S_y=default_payoffs.get('Y')):
    """
    Computes the stationary probability distribution for Markov chain
    corresponding to the PD game, and returns the long-term expected value.

    Note: S_x, S_y are expected to be row vectors of shape (1, m)

    :param S_x: short-term payoffs for X, else uses literature defaults.
    :param S_y: short-term payoffs for Y, else uses literature defaults.

    :return: tuple - The long-term payoffs for X, Y, respectively.
    """
    # M represents the transition matrix for the Markov chain
    M = np.array([[.30, .70],
                  [.75, .25]])

    # compute the left eigenvector of M with a corresponding eigenvalue
    # of 1 (λ=1). i.e. np.dot(v, M) = λv
    e_vals, e_vecs = np.linalg.eig(M.T)

    # grab eigenvector corresponding to λ=1
    # —currently assumes 0th element contains stationary_vec,
    # this might be a false assumption
    # TODO: Bake a better fail-safe check for this into here.
    stationary_vec = np.real(e_vecs[:, 0])

    # reshape stationary_vec for dotting with payoffs
    # defaults to a rank-1 vector which is no good
    stationary_vec = stationary_vec.reshape(stationary_vec.shape[0], -1)

    # Check that the eigenvector has been computed correctly
    if debug:
        sstate = np.dot(stationary_vec.T, M)

        # perform element-wise comparison
        for i, element in enumerate(sstate[0]):
            x = round(element, 3)
            y = round(stationary_vec[i][0], 3)

            print('Checking assertion of x, y...')
            assert(x == y)
            print('... x == y!')

    exp_value = (stationary_vec.dot(S_x),
                 stationary_vec.dot(S_y))

    return exp_value


compute_equilibrium_payoffs()