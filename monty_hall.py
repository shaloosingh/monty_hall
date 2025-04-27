import random
import tkinter as tk
from tkinter import messagebox

def simulate(strategy, num_trials):
    """Simulate the Monty Hall problem."""
    wins = 0
    for _ in range(num_trials):
        doors = [0, 0, 0]
        prize_door = random.randint(0, 2)
        doors[prize_door] = 1

        player_choice = random.randint(0, 2)

        # Host opens a door with a goat
        available_doors = [i for i in range(3) if i != player_choice and doors[i] == 0]
        host_opens = random.choice(available_doors)

        # If switching
        if strategy == 'switch':
            remaining_doors = [i for i in range(3) if i != player_choice and i != host_opens]
            player_choice = remaining_doors[0]

        if doors[player_choice] == 1:
            wins += 1
    return wins

def run_simulation():
    strategy = strategy_var.get()
    try:
        num_trials = int(entry_trials.get())
        if num_trials <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive integer for number of trials.")
        return

    wins = simulate(strategy, num_trials)
    win_percentage = (wins / num_trials) * 100

    result_text.set(f"Strategy: {strategy.capitalize()}\n"
                    f"Trials: {num_trials}\n"
                    f"Wins: {wins}\n"
                    f"Win Rate: {win_percentage:.2f}%")

# --- GUI Setup ---
root = tk.Tk()
root.title("Monty Hall Problem Simulator 🎁🚪")
root.geometry("400x350")
root.resizable(False, False)

# Title
tk.Label(root, text="Monty Hall Simulator", font=("Helvetica", 18, "bold")).pack(pady=10)

# Strategy selection
strategy_var = tk.StringVar(value="switch")
tk.Label(root, text="Choose Strategy:").pack()

frame_strategy = tk.Frame(root)
frame_strategy.pack()

tk.Radiobutton(frame_strategy, text="Always Switch", variable=strategy_var, value="switch").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame_strategy, text="Always Stay", variable=strategy_var, value="stay").pack(side=tk.LEFT, padx=10)

# Number of trials input
tk.Label(root, text="Number of Trials:").pack(pady=5)
entry_trials = tk.Entry(root, justify="center")
entry_trials.insert(0, "1000")
entry_trials.pack(pady=5)

# Run button
tk.Button(root, text="Run Simulation", command=run_simulation, bg="lightblue", font=("Helvetica", 12, "bold")).pack(pady=10)

# Result display
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 12), justify="center")
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()
