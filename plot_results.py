import numpy as np
import matplotlib.pyplot as plt

from compute_payoffs import compute_equilibrium_payoffs
from default_settings import strategies

s = [x for x in strategies.keys()]
x = [strategies.get(key).get('X') for key in s]
y = [strategies.get(key).get('Y') for key in s]

# store X's score
score = np.eye(len(s))

# store net score
net_score = np.eye(len(s))

for i, s_x in enumerate(s):
    for j, s_y in enumerate(s):
        p = compute_equilibrium_payoffs(np.array(strategies.get(s_x).get('X')),
                                        np.array(strategies.get(s_y).get('Y')))

        net_score[i, j] = p[0] + p[1]
        score[i, j] = p[0]

fig = plt.figure()
ax = fig.add_subplot(121)

vmax = 5
cax = ax.matshow(score.T, vmin=1, vmax=vmax, cmap='hot')
fig.colorbar(cax)

ax.set_xticklabels(['']+s)
ax.set_yticklabels(['']+s)
ax.set_title('X\'s payoff')

ax.set_xlabel('X plays')
ax.set_ylabel('Y plays')

ax = fig.add_subplot(122)

vmax = 6
cax = ax.matshow(net_score.T, vmin=1, vmax=vmax, cmap='hot')
fig.colorbar(cax)

ax.set_xticklabels(['']+s)
ax.set_yticklabels(['']+s)

ax.set_xlabel('X plays')
ax.set_ylabel('Y plays')

ax.set_title('Net payoffs')

plt.show()