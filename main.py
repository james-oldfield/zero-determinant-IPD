import numpy as np

from argparse import ArgumentParser
from default_settings import defaults

parser = ArgumentParser(description='')
parser.add_argument('--debug', required=False)
args = parser.parse_args()

debug = args.debug


def compose_markov_mat(p, q):
    """
    Creates a markov matrix specified by probability vectors
    of cooperating, p, q.

    :param p: prob. of cooperating, given (cc, cd, dc, dd) in last time step
    :param q: prob. of cooperating, given (cc, cd, dc, dd) in last time step

    :return: matrix - numpy matrix representing transitions
    """
    p1, p2, p3, p4 = p
    q1, q2, q3, q4 = q

    return np.array([[p1*q1, p1*(1.0-q1), (1.0-p1)*q1, (1-p1)*(1-q1)],
                     [p2*q3, p2*(1.0-q3), (1.0-p2)*q3, (1-p2)*(1-q3)],
                     [p3*q2, p3*(1.0-q2), (1.0-p3)*q2, (1-p3)*(1-q2)],
                     [p4*q4, p4*(1.0-q4), (1.0-p4)*q4, (1-p4)*(1-q4)]])


def compute_equilibrium_payoffs(S_x=defaults.get('X'),
                                S_y=defaults.get('Y'),
                                p=defaults.get('p'),
                                q=defaults.get('q')):
    """
    Computes the stationary probability distribution for Markov chain
    corresponding to the PD game, and returns the long-term expected value.

    Note: S_x, S_y are expected to be row vectors of shape (1, m)

    :param S_x: short-term payoffs for X, else uses literature defaults.
    :param S_y: short-term payoffs for Y, else uses literature defaults.

    :return: tuple - The long-term payoffs for X, Y, respectively.
    """

    M = compose_markov_mat(p, q)

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

    # normalise to constitute valid prob. dist
    stationary_vec = stationary_vec / sum(stationary_vec)

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

    exp_value = (stationary_vec.T.dot(S_x.T),
                 stationary_vec.T.dot(S_y.T))

    return exp_value


compute_equilibrium_payoffs()