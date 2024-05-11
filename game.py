import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("350x500")

        self.buttons = []
        self.who = 'X'
        self.spots = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.score = {'X': 0, 'O': 0}
        self.game_started = False

        self.start_screen()

    def start_screen(self):
        start_label = tk.Label(self.root, text="Welcome to Tic Tac Toe", font=("Arial", 12))
        start_label.grid(row=0, column=0, padx=2, pady=2)
        instructions_text = """Instructions:
               - The game is played on a 3x3 grid.
               - Player X and Player O take turns marking the spaces.
               - The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.
               - If all 9 spaces are filled and no player has achieved a winning pattern, the game is a draw."""
        self.instructions_label = tk.Label(self.root, text=instructions_text, font=("Arial", 12))
        self.instructions_label.grid(row=1, column=0, padx=5, pady=5)

        start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        start_button.grid(row=2, column=0, padx=5, pady=5)

    def start_game(self):
        self.game_started = True
        self.instructions_label.config(text="")
        self.board()
        self.statistics()

    def board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 20), width=1, height=1,
                                   command=lambda row=i, col=j: self.click_button(row, col))
                button.grid(row=i + 2, column=j, sticky="nsew", padx=5, pady=5)
                self.buttons.append(button)

    def statistics(self):
        self.turn_label = tk.Label(self.root, text="Turn: X", font=("Arial", 12))
        self.turn_label.grid(row=0, column=0, padx=5)

        self.score_label = tk.Label(self.root, text="Score: X - 0 | O - 0", font=("Arial", 12))
        self.score_label.grid(row=1, column=0, padx=5)

    def switch(self):
        if self.who == 'X':
            self.who = 'O'
        else:
            self.who = 'X'

    def click_button(self, row, col):
        if self.game_started and self.spots[row * 3 + col] == '-':
            self.spots[row * 3 + col] = self.who
            self.buttons[row * 3 + col].config(text=self.who)
            self.switch()
            self.check_win()
            self.update_turn_label()

    def update_turn_label(self):
        self.turn_label.config(text=f"Turn: {self.who}")

    def check_win(self):
        winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for combo in winning_combinations:
            if self.spots[combo[0]] == self.spots[combo[1]] == self.spots[combo[2]] != '-':
                winner = self.spots[combo[0]]
                self.score[winner] += 1
                self.update_score_label()
                self.game_over_screen(f"{winner} wins!")
                return

        if '-' not in self.spots:
            self.show_game_over_screen("It's a draw!")

    def update_score_label(self):
        self.score_label.config(text=f"Score: X - {self.score['X']} | O - {self.score['O']}")

    def game_over_screen(self, message):
        game_over_screen = tk.Toplevel(self.root)
        game_over_screen.title("Game Over")
        game_over_screen.geometry("200x200")

        label = tk.Label(game_over_screen, text=message, font=("Arial", 16))
        label.pack(pady=10)

        score_label = tk.Label(game_over_screen, text=f"Final Scores: X - {self.score['X']} | O - {self.score['O']}", font=("Arial", 12))
        score_label.pack(pady=5)

        start_over_button = tk.Button(game_over_screen, text="Start Over", command=self.start_over)
        start_over_button.pack(pady=5)

    def start_over(self):
        self.root.destroy()
        self.__init__()
        self.start_screen()

    def play(self):
        self.root.mainloop()

def main():
    game = TicTacToe()
    game.play()

if __name__ == "__main__":
    main()

