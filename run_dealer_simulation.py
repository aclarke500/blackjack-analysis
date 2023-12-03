from Dealer import Dealer, Match

dealers = [Dealer(i, f"Dealer {i}") for i in range(1, 22)]

match_matrix = []

for d1 in dealers:
  match_row = []
  for d2 in dealers:
    ma = Match(d1, d2, f"{d1.name} vs {d2.name}", 10)
    match_row.append(ma)
  match_matrix.append(match_row)



   

