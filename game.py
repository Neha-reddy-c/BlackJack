print("Welcome to BlackJack!")
import art
import random


def game():
    phand = []
    chand = []
    end = False
    print(art.blackjack_logo)
    def deal():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        random.shuffle(cards)
        hand = random.choice(cards)
        return hand

    def score(hand):
        if sum(hand) == 21 and len(hand) == 2:
            return 0
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
        return sum(hand)

    def compare(csum, psum):
        if psum == csum:
            return "Draw 🙃"
        elif csum == 0:
            return "Lose, opponent has Blackjack 😱"
        elif psum == 0:
            return "Win with a Blackjack 😎"
        elif psum > 21:
            return "You went over. You lose 😭"
        elif csum > 21:
            return "Opponent went over. You win 😁"
        elif psum > csum:
            return "You win 😃"
        else:
            return "You lose 😤"

    for i in range(2):
        phand.append(deal())
        chand.append(deal())

    while end == False:
        psum = score(phand)
        csum = score(chand)

        print(f"Your cards are: {phand}     Your score is: {psum}")
        print(f"Computer's first card is: {chand[0]}")

        if psum == 0 or csum == 0 or psum > 21:
            end = True
        else:
            more = input("Would you like to get another card? 'Y' or 'N' \n").upper()
            if more == "Y":
                phand.append(deal())
            else:
                end = True

    while csum != 0 and csum < 17:
        chand.append(deal())
        csum = score(chand)

    print(f"Your final cards are: {phand}     Your score is: {psum}")
    print(f"Computer's final cards are: {chand}     Your score is: {csum}")
    print(compare(csum, psum))
    print("\n" * 5)

while input("Would you like to play a game of BlackJack? 'Y' or 'N' \n").upper() == "Y":
    game()
