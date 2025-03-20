print("This is a number guessing game")
import random

random_num = random.randint(1, 100)

def NumberGuess():
    try:
        guess = int(input("Guess a number between 1 to 100 (Type 0 to exit): "))

        if guess == 0:
            print("Game Exited. Thanks for playing!")
            return  # ❌ Pehle yeh exit nahi ho raha tha
        
        if guess < 1 or guess > 100:
            print("❌ Enter a number between 1 and 100!")
            return NumberGuess()  # ✅ Return kar rahe hain taake function properly restart ho
        
        if guess > random_num:
            print("📈 Too High! Try Again.")
            return NumberGuess()
        
        if guess < random_num:
            print("📉 Too Low! Try Again.")
            return NumberGuess()

        print("🎉 Congratulations! You guessed the correct number:", random_num)

    except ValueError:
        print("❌ Invalid Input! Please enter a valid number.")
        return NumberGuess()  # ✅ Invalid input par dobara function call hoga

# Start the game
try:
    NumberGuess()
except Exception as e:
    print(f"An error occurred: {e}")

print(f"The correct number was: {random_num}")
