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
    },
    'ws-ls': {
        'X': (1, 0, 0, 1),
        'Y': (1, 0, 0, 1),
    },
    # (approximation of in memory-1)
    'grim': {
        'X': (1, 0, 0, 0),
        'Y': (1, 0, 0, 0),
    },
    'ex-3': {
        'X': (0.8461538461538461, 0.5, 0.2692307692307692, 0),
        'Y': (0.8461538461538461, 0.2692307692307692, 0.5, 0),
    },
    'defect': {
        'X': (0, 0, 0, 0),
        'Y': (0, 0, 0, 0)
    },
    'coop': {
        'X': (1, 1, 1, 1),
        'Y': (1, 1, 1, 1)
    }
}
