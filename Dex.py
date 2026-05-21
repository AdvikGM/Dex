import random

# 📚 DICTIONARY DATABASE (For regular chatting)
chat_data = {
    "Hello": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
    "Hi": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
    "Good": ["That's awesome! I'm happy to hear that.", "Sweet! Good vibes only."],
    "Sad": ["I'm sorry to hear that. Sending a virtual hug! 🤗", "Cheer up! You got this!"],
    "Tired": ["Go get some rest! 😴", "Take a break, coding can wait."]
}

print("🤖 Action-Bot Activated!")
print("Commands you can try: 'Flip', 'Roll', 'Rps', or 'Exit'")
print("=" * 60)

while True:
    raw_input = input("\n[Chat] You 👤: ").strip()
    
    if not raw_input:
        continue
        
    # Capitalizes ONLY the very first letter of your sentence
    user_input = raw_input[0].upper() + raw_input[1:]
    
    # 1. EXIT COMMAND
    if user_input == "Exit":
        print("\nBot: Goodbye! Have a great day.")
        break
        
    # 2. FEATURE 1: COIN FLIPPER 🪙
    elif user_input == "Flip":
        result = random.choice(["🪙 HEADS!", "🪙 TAILS!"])
        print(f"Bot: Flipping a coin... It landed on: {result}")
        print("-" * 30)

    # 3. FEATURE 2: ROCK, PAPER, SCISSORS ✊✋✌️
    elif user_input == "Rps":
        player_choice = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        
        if player_choice in ["Rock", "Paper", "Scissors"]:
            bot_choice = random.choice(["Rock", "Paper", "Scissors"])
            print(f"Bot chose: {bot_choice}")
            
            # Check who won
            if player_choice == bot_choice:
                print("Bot: 👔 It's a tie!")
            elif (player_choice == "Rock" and bot_choice == "Scissors") or \
                 (player_choice == "Paper" and bot_choice == "Rock") or \
                 (player_choice == "Scissors" and bot_choice == "Paper"):
                print("Bot: 🎉 You win!")
            else:
                print("Bot: 🤖 I win!")
        else:
            print("Bot: ⚠️ Invalid choice! Please type Rock, Paper, or Scissors.")
        print("-" * 30)

    # 4. FEATURE 3: DICE ROLLER 🎲
    elif user_input == "Roll":
        dice_number = random.randint(1, 6)
        print(f"Bot: 🎲 You rolled a: {dice_number}")
        print("-" * 30)

    
    else:
        found_answer = False
        
        for key in chat_data:
            if key in user_input:
                bot_reply = random.choice(chat_data[key])
                print(f"Bot: {bot_reply}")
                found_answer = True
                break
        
        if not found_answer:
            print("Bot: I don't know that command yet. Try typing 'Flip', 'Roll', or 'Rps'!")
