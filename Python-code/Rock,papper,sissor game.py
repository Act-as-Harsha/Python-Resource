import random
import time

# Define choices and their names
choices = ["Rock", "Paper", "Scissors"]
emojis = ["🪨", "📄", "✂️"]

# Show instructions
print("🎮 Welcome to Rock, Paper, Scissors! 🎮")
print("Choose your move:")
print("0 = Rock 🪨")
print("1 = Paper 📄")
print("2 = Scissors ✂️")
print("-" * 35)

# Get user input with validation
try:
    user_choice = int(input("Enter your choice (0-2): "))
    if user_choice not in [0, 1, 2]:
        raise ValueError
except ValueError:
    print("❌ Invalid input! Please run the game again and enter 0, 1, or 2.")
    exit()

# Computer's random choice
computer_choice = random.randint(0, 2)

# Dramatic pause
print("\n🧠 Computer is making a move", end="")
for _ in range(3):
    print(".", end="", flush=True)
    time.sleep(0.5)

# Show choices
print(f"\n\nYou chose: {emojis[user_choice]} {choices[user_choice]}")
print(f"Computer chose: {emojis[computer_choice]} {choices[computer_choice]}")

# Decide outcome
if user_choice == computer_choice:
    print("😐 It's a draw!")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):
    print("🎉 You win!")
else:
    print("💻 Computer wins!")

# End
print("\nThanks for playing! 👋")
