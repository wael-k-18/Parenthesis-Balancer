
# 🌟 Balanced Parentheses Game 🌟

This is a simple Python game where players can check if the parentheses in a given string are balanced or not. The game uses a **Pushdown Automaton (PDA)** to simulate the process of balancing parentheses and provides real-time feedback to the player.

### Features:
- **Interactive GUI**: Built using Tkinter, with an engaging interface.
- **Real-time PDA Simulation**: Shows the steps of the PDA as it evaluates the input string.
- **Score Tracking**: The game keeps track of your score based on the correctness of the input.
- **Detailed Feedback**: Provides step-by-step feedback on the PDA transitions and stack operations.

### Requirements:
- **Python 3.x**
- **Tkinter** (usually comes pre-installed with Python)

If you don't have Tkinter installed, you can install it using:
```bash
pip install tk
```

### Game Flow:
1. **Start Game**: Starts the game and allows the user to enter a string of parentheses.
2. **Check Parentheses**: When the user submits a string, the PDA evaluates if the parentheses are balanced.
3. **Reset Input**: Clears the input field and allows the user to enter a new string.
4. **End Game**: Ends the game, shows the final score, and resets the score for the next round.

### How It Works:
The game simulates a **Pushdown Automaton (PDA)** with the following logic:
- The PDA uses a stack to handle the parentheses. 
- For every opening parenthesis `(`, it is pushed to the stack.
- For every closing parenthesis `)`, it pops from the stack if there’s an opening parenthesis to match.
- If the stack is empty after processing the string, the parentheses are balanced.

### Game Instructions:
1. Launch the game.
2. Type a string of parentheses in the input field (e.g., `(()())`).
3. Click "🔍 Check Parentheses" to see if the string is balanced.
4. If the parentheses are balanced, you'll see a success message with an emoji 🎉✅.
5. If the parentheses are unbalanced, you'll see a rejection message with an emoji ❌👎.
6. Reset the input or end the game anytime.

Enjoy the game! 🎮
