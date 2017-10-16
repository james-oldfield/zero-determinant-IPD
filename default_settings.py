import numpy as np


defaults = {
    # Define the standard short-term payoff vectors for a PD
    'X': np.array([[5, 3, 1, 0]]),
    'Y': np.array([[5, 1, 3, 0]]),

    # Default probs. for cooperating
    'p': (1, 0, 1, 0),
    'q': (1, 1, 0, 0),
}
