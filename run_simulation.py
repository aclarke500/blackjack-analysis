import pandas as pd
import random
df = pd.read_csv('cards.csv')
# convert dataframe to list of tuples
cards = list(df.itertuples(index=False, name=None))
number_of_cards = len(cards)


def run_game(bust_value: int) -> int:
  cards = list(df.itertuples(index=False, name=None))
  score = 0
  # get random card from deck
  card = random.choice(cards)
  # remove card from deck
  cards.remove(card)
  while score < bust_value:
    # get card value
    card_value = get_card_value(card, score, bust_value)
    # add card value to score
    score += card_value
    # get random card from deck
    card = random.choice(cards)
    # remove card from deck
    cards.remove(card)

  if score > 21:
    return 0
  else:
    return score

def get_card_value(card: tuple, score: int, bust_value: int) -> int:
  # get card value
  card_value = card[1]
  # convert card value to int
  if card_value in ['Jack', 'Queen', 'King']:
    card_value = 10
  elif card_value == 'Ace':
    if score + 11 > bust_value:
      card_value = 1
    card_value = 11
  else:
    card_value = int(card_value)
  return card_value


max_values = [i for i in range(1, 22)]
results = []
for i in max_values:
  results_for_i = []
  for j in range(10000):
    results_for_i.append(run_game(i))
  results.append(results_for_i)

my_dict = {max_values[i]: results[i] for i in range(len(max_values))}
print(my_dict)

df = pd.DataFrame(my_dict)
df.to_csv('results.csv', index=False)


# res_dict = {}
# for i in range(len(max_values)):
#   res_dict[str(max_values[i])] = results[i]

# df = pd.DataFrame(results, index=max_values)
# df.to_csv('results.csv', index=False)
