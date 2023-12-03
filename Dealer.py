import pandas as pd
from game_library import turn, df


class Dealer:
    def __init__(self, threshold, name):
        self.threshold = threshold
        self.name = name

class Match:
    def __init__(self, dealer, player, name, trials):
        self.dealer = dealer
        self.player = player
        self.name = name
        self.dealer_wins = 0
        self.player_wins = 0
        self.results = []

        for i in range(trials):
            self.results.append(self.run_game())


    
    def run_game(self):
      cards = list(df.itertuples(index=False, name=None))
      # player goes
      player_score = turn(self.player.threshold, cards, 0)
      # dealer goes
      dealer_score = turn(self.dealer.threshold, cards, 0)

      if player_score > 21:
          return [True, False]
      elif dealer_score > 21:
          return [False, True]
      elif player_score > dealer_score:
          return [False, True]
      elif dealer_score > player_score:
          return [True, False]
      else:
          return [False, False]

    def interpret_results(self, results):
      # results = [dealer_wins, player_wins]
      for result in results:
        if result[0]:
          self.dealer_wins += 1
        if result[1]:
          self.player_wins += 1