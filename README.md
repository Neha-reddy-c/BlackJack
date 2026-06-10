# BlackJack Game 🃏

A command-line implementation of the classic casino card game, Blackjack (also known as 21), written in Python.

## 🎮 How to Play

The goal of Blackjack is to beat the computer's (dealer's) hand without going over 21.

1. **The Deal:** Both you and the computer are dealt two cards. You can see both of your cards, but only the computer's first card.
2. **Hit or Stand:** You will be asked if you want to take another card (`'Y'`) or pass (`'N'`). You can keep drawing cards as long as your total score is under 21.
3. **The Dealer's Turn:** Once you choose to stand, the computer will automatically draw cards until its total score is "x" or higher.
4. **Determining the Winner:** The game compares the final scores to declare a winner, a loss, or a draw.

## 📜 Game Rules Used

* **Card Values:** Number cards are worth their face value. Face cards (Jack, Queen, King) are worth 10. 
* **The Ace:** An Ace can count as either 11 or 1 depending on whether your total score exceeds 21.
* **Natural Blackjack:** Getting an Ace and a 10-value card right on the deal counts as a score of `0` in the logic, securing an automatic win (unless the dealer also has one).
* **Dealer Strategy:** The computer must hit on any hand lower than "x".

## 🛠️ Prerequisites

Before running the game, make sure you have Python installed on your system. You will also need the accompanying `art.py` file in the same directory for the game's logo to display correctly.

## 🚀 Running the Game

1. Clone or download this repository.
2. Open your terminal or command prompt and navigate to the project directory.
3. Run the following command:

```bash
python game.py
