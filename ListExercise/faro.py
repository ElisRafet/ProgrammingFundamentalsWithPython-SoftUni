cards = input().split(' ')
shuffles = int(input())

left_side = []
right_side = []
#new_cards = []
#
# for current_shuffles in range(shuffles):
#     mid_cards = len(cards) // 2
#     left_side = cards[:mid_cards]
#     right_side = cards[mid_cards:]
#
# for card_index in range(len(right_side)):
#     new_cards.append(left_side[card_index])
#     new_cards.append(right_side[card_index])
#
# print(new_cards)
for current_shuffles in range(shuffles):
     mid_cards = len(cards) // 2
     left_side = cards[:mid_cards]
     right_side = cards[mid_cards:]
     new_cards = []
     for card_index in range(len(right_side)):
         new_cards.append(left_side[card_index])
         new_cards.append(right_side[card_index])
     cards = new_cards

print(cards)