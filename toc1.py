import tkinter as tk
from tkinter import messagebox
import random

# Game Emojis and Colors
EMOJIS = {"accepted": "🎉✅", "rejected": "❌👎"}
BG_COLORS = {"menu": "#0B3D91", "game": "#FFEBEE"}
TEXT_COLORS = {"primary": "#FFD700", "secondary": "#FF5722"}

class PDA:
    def __init__(self):
        self.stack = ["$"]
        self.state = "q0"
        self.score = 0

    def transition(self, symbol, verbose_output):
        if self.state == "q0":
            verbose_output.append(f"Reading '{symbol}', Stack before: {self.stack}")
            if symbol == "(":
                self.stack.append("(")
            elif symbol == ")" and self.stack[-1] == "(":
                self.stack.pop()
            else:
                self.state = "REJECTED"
            verbose_output.append(f"Stack after: {self.stack}\n")

    def check_balanced_parentheses(self, input_string):
        verbose_output = []
        for char in input_string:
            self.transition(char, verbose_output)
        if self.state != "REJECTED" and self.stack == ["$"]:
            self.score += 10
            return "ACCEPTED", verbose_output
        else:
            self.score -= 5
            return "REJECTED", verbose_output

    def reset(self):
        self.stack = ["$"]
        self.state = "q0"

class PDAApp:
    def __init__(self, root):
        self.pda = PDA()
        self.root = root
        self.root.title("🌟 Balanced Parentheses Game 🌟")
        self.create_menu()

    def create_menu(self):
        self.root.configure(bg=BG_COLORS["menu"])
        title_label = tk.Label(self.root, text="Balanced Parentheses Game", font=("Arial", 24, "bold"), bg=BG_COLORS["menu"], fg=TEXT_COLORS["primary"])
        title_label.pack(pady=30)

        start_button = tk.Button(self.root, text="🎮 Start Game", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white", command=self.start_game)
        start_button.pack(pady=20)

        quit_button = tk.Button(self.root, text="🚪 Quit Game", font=("Arial", 18, "bold"), bg="#FF5722", fg="white", command=self.root.quit)
        quit_button.pack(pady=10)

    def start_game(self):
        self.clear_screen()
        self.root.configure(bg=BG_COLORS["game"])
        self.create_game_interface()

    def create_game_interface(self):
        title_label = tk.Label(self.root, text="Balanced Parentheses Checker Game", font=("Arial", 18, "bold"), bg=BG_COLORS["game"], fg="#2196F3")
        title_label.pack(pady=15)

        self.input_field = tk.Entry(self.root, font=("Arial", 14), width=30, bd=2, relief="groove")
        self.input_field.pack(pady=10)
        self.input_field.focus()

        check_button = tk.Button(self.root, text="🔍 Check Parentheses", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=self.check_parentheses)
        check_button.pack(pady=10)

        reset_button = tk.Button(self.root, text="🔄 Reset", font=("Arial", 14, "bold"), bg="#FF5722", fg="white", command=self.reset_input)
        reset_button.pack(pady=5)

        end_game_button = tk.Button(self.root, text="🏁 End Game", font=("Arial", 14, "bold"), bg="#E53935", fg="white", command=self.end_game)
        end_game_button.pack(pady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 16), bg=BG_COLORS["game"])
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self.root, text=f"Score: {self.pda.score}", font=("Arial", 14, "bold"), bg=BG_COLORS["game"], fg="#4CAF50")
        self.score_label.pack(pady=5)

        self.verbose_output = tk.Text(self.root, font=("Arial", 12), height=8, width=40, state=tk.DISABLED, bd=0, wrap="word")
        self.verbose_output.pack(pady=10)

    def check_parentheses(self):
        input_string = self.input_field.get()
        self.pda.reset()
        result, verbose_output = self.pda.check_balanced_parentheses(input_string)

        emoji = EMOJIS["accepted"] if result == "ACCEPTED" else EMOJIS["rejected"]
        self.result_label.config(text=f"{result} {emoji}", fg="green" if result == "ACCEPTED" else "red")
        self.score_label.config(text=f"Score: {self.pda.score}")

        self.verbose_output.config(state=tk.NORMAL)
        self.verbose_output.delete(1.0, tk.END)
        for line in verbose_output:
            self.verbose_output.insert(tk.END, line + "\n")
        self.verbose_output.config(state=tk.DISABLED)

    def reset_input(self):
        self.input_field.delete(0, tk.END)
        self.result_label.config(text="")
        self.verbose_output.config(state=tk.NORMAL)
        self.verbose_output.delete(1.0, tk.END)
        self.verbose_output.config(state=tk.DISABLED)

    def end_game(self):
        messagebox.showinfo("Game Over", f"Game Ended! Your final score is {self.pda.score}")
        self.pda.score = 0  # Reset score
        self.clear_screen()
        self.create_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = PDAApp(root)
    root.mainloop()
