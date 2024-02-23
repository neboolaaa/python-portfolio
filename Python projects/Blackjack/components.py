logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\_
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

import random
def deal_card():
  """Returns random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,]
  card_number = random.choice(cards)
  return card_number

def ace_move(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, dealer_score):
  if user_score == dealer_score and dealer_score !=21:
    return "It's a draw!"
  elif user_score == dealer_score and dealer_score == 21:
    return "You both have Blackjack, rules say that dealer wins!"
  elif dealer_score == 21:
    return "You lose, the dealer has Blackjack!"
  elif user_score == 21 and dealer_score !=21:
    return "You win with a Blackjack!"
  elif user_score > 21:
    return "You went over. You're bust!"
  elif dealer_score > 21:
    return "Dealer went over. You win!"
  elif user_score > dealer_score:
    return "You scored higher than the dealer, and so you win!"
  else:
    return "The dealer scored higher than you, so you lose!"


                                      
     