from components import logo, ace_move, deal_card, compare
import time

def play_game():
  print(logo)
  time.sleep(1.3)
  user_card = []
  dealer_card = []
  is_game_over = False
  for _ in range(2):
    user_card.append(deal_card())
    dealer_card.append(deal_card())
  while not is_game_over:
    user_score = ace_move(user_card)
    dealer_score = ace_move(dealer_card)
    while dealer_score != 21 and dealer_score < 17:
      dealer_card.append(deal_card())
      dealer_score = ace_move(dealer_card)
    print(f"Your first two cards: {user_card}, current total: {user_score}")
    time.sleep(0.3)
    print(f"Computer's first card: {dealer_card[0]}, but you don't know his second card!")
    if user_score == 21 or dealer_score == 21 or user_score > 21:
      time.sleep(0.4)
      is_game_over = True
    else:
      time.sleep(0.4)
      user_should_deal = input("Would you like to hit or stand? ").lower()
      if user_should_deal == "hit":
        print("\033c")
        print(logo)
        user_card.append(deal_card())
        user_score = ace_move(user_card)
        is_game_over = True
      else:
        print("\033c")
        print(logo)
        is_game_over = True
  print(f"Your final hand: {user_card}, making your final score: {user_score}")
  print(f"Computer's final hand: {dealer_card}, making their final score: {dealer_score}")
  print(compare(user_score, dealer_score))

while input("Do you want to play Blackjack? Y/N ").lower() == "y":
  print("\033c")
  time.sleep(0.1)
  play_game()
            
