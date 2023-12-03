import pandas as pd

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
card_values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

cards = []
for suit in suits:
    for value in card_values:
        cards.append([suit, value])

df = pd.DataFrame(cards, columns=['Suit', 'Value'])
df.to_csv('cards.csv', index=False)