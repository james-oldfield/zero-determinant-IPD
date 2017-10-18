import numpy as np


defaults = {
    # Define the standard short-term payoff vectors for a PD
    'X': np.array([[3, 0, 5, 1]]),
    'Y': np.array([[3, 5, 0, 1]]),
}

# specifies hard-coded strategies for use
strategies = {
    'tft': {
        'X': (1, 0, 1, 0),
        'Y': (1, 1, 0, 0),
    }
}
