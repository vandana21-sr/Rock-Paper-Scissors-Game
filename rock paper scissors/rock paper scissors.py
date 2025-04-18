import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the result
def play_game(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Main window setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Instructions label
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
instructions.pack(pady=20)

# Images
rock_img = tk.PhotoImage(file="rock.jpg")
paper_img = tk.PhotoImage(file="paper.jpg")
scissors_img = tk.PhotoImage(file="scissors.jpg")

# Buttons for user choices
rock_button = tk.Button(root, image=rock_img, command=lambda: play_game('rock'))
rock_button.pack(side=tk.LEFT, padx=20)

paper_button = tk.Button(root, image=paper_img, command=lambda: play_game('paper'))
paper_button.pack(side=tk.LEFT, padx=20)

scissors_button = tk.Button(root, image=scissors_img, command=lambda: play_game('scissors'))
scissors_button.pack(side=tk.LEFT, padx=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

# Start the GUI event loop
root.mainloop()
