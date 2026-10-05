import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pro Tic Tac Toe")
        self.window.configure(bg="#2c3e50")  # Dark slate background

        # Game State
        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        # Colors
        self.color_bg = "#2c3e50"
        self.color_btn = "#34495e"
        self.color_text = "#ecf0f1"
        self.color_x = "#e74c3c"  # Red
        self.color_o = "#3498db"  # Blue

        self.create_widgets()

    def create_widgets(self):
        # Status Label to show whose turn it is
        self.label = tk.Label(
            self.window,
            text=f"Player {self.current_player}'s Turn",
            font=("Arial", 14, "bold"),
            bg=self.color_bg,
            fg=self.color_text,
            pady=20
        )
        self.label.pack()

        # Container for the grid
        self.grid_frame = tk.Frame(self.window, bg=self.color_bg)
        self.grid_frame.pack(padx=20, pady=10)

        # Create a 3x3 grid of buttons
        for i in range(9):
            btn = tk.Button(
                self.grid_frame,
                text="",
                font=("Arial", 24, "bold"),
                width=4,
                height=1,
                bg=self.color_btn,
                fg=self.color_text,
                relief="flat",
                activebackground="#4e6a85",
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Reset button
        self.reset_btn = tk.Button(
            self.window,
            text="Restart Game",
            font=("Arial", 12),
            bg="#95a5a6",
            fg="white",
            relief="flat",
            padx=20,
            command=self.reset_game
        )
        self.reset_btn.pack(pady=20)

    def on_click(self, index):
        if self.board[index] == "":
            # Update state
            self.board[index] = self.current_player

            # Set color based on player
            color = self.color_x if self.current_player == "X" else self.color_o
            self.buttons[index].config(text=self.current_player, fg=color)

            if self.check_winner():
                self.label.config(text=f"🎉 Player {self.current_player} Wins!", fg="#f1c40f")
                self.disable_board()
                messagebox.showinfo("Winner!", f"Congratulations! Player {self.current_player} won the game!")
                self.reset_game()
            elif "" not in self.board:
                self.label.config(text="🤝 It's a Draw!", fg="#bdc3c7")
                messagebox.showinfo("Draw", "No one wins this time!")
                self.reset_game()
            else:
                # Switch players
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Cols
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def disable_board(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.label.config(text=f"Player {self.current_player}'s Turn", fg=self.color_text)
        for btn in self.buttons:
            btn.config(text="", state="normal", bg=self.color_btn)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.run()
