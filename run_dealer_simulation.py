from Dealer import Dealer, Match
import matplotlib.pyplot as plt
import numpy as np

number_of_matches = 100 # number of matches to run


dealers = [Dealer(i, f"Dealer {i}") for i in range(1, 22)]
match_matrix = []

for d1 in dealers:
  match_row = []
  for d2 in dealers:
    ma = Match(d1, d2, f"{d1.name} vs {d2.name}", number_of_matches)
    if ma.dealer_wins == 0:
      match_row.append(1)
    else:
      match_row.append((ma.player_wins/ma.dealer_wins)/number_of_matches)
  match_matrix.append(match_row)

matrix = np.array(match_matrix)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a 3D bar plot
_x = np.arange(matrix.shape[1])
_y = np.arange(matrix.shape[0])
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = matrix.ravel()
bottom = np.zeros_like(top)
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)

# Labels and titles (optional)
ax.set_xlabel('Dealer')
ax.set_ylabel('Player')
ax.set_zlabel('Probability of Winning')
ax.set_title(f'Results of {number_of_matches} matches between dealers and players')

plt.show()


   

