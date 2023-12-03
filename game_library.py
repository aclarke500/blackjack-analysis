import pandas as pd
import random

df = pd.read_csv('cards.csv')
# convert dataframe to list of tuples
cards = list(df.itertuples(index=False, name=None))
number_of_cards = len(cards)


def deal_card(cards):
    card = random.choice(cards)
    cards.remove(card)
    return card

def turn(threshold, cards, score):
    while score < threshold:
        card = deal_card(cards)
        card_value = get_card_value(card, score, threshold)
        score += card_value
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


# def run_game(dealer, player):
#     cards = list(df.itertuples(index=False, name=None))
#     # player goes
#     player_score = turn(player.threshold, cards, 0)
#     # dealer goes
#     dealer_score = turn(dealer.threshold, cards, 0)

#     if player_score > 21:
#         return [True, False]
#     elif dealer_score > 21:
#         return [False, True]
#     elif player_score > dealer_score:
#         return [False, True]
#     elif dealer_score > player_score:
#         return [True, False]
#     else:
#         return [False, False]

    