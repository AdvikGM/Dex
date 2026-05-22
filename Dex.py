from datetime import datetime
import random
import time

# 📚 DICTIONARY DATABASE (For regular chatting)
chat_data = {
    "Hello": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
    "Hi": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
    "Good": ["That's awesome! I'm happy to hear that.", "Sweet! Good vibes only."],
    "Sad": ["I'm sorry to hear that. Sending a virtual hug! 🤗", "Cheer up! You got this!"],
    "Tired": ["Go get some rest! 😴", "Take a break, coding can wait."]
}

# 👤 USER STATE & UTILITIES
user_name = "User"
todo_list = []  
VERSION = "v2.7.5"

print(f"🤖 Dex: Assistant Bot Activated! [{VERSION}]")
print("Type 'Help' to see all my utility and game features!")
print("=" * 60)

while True:
    raw_input = input(f"\n[Chat] {user_name} 👤: ").strip()
    
    if not raw_input:
        continue
        
    user_input = raw_input[0].upper() + raw_input[1:]
    
    # EXIT COMMAND
    if user_input == "Exit":
        print(f"\nDex: Goodbye {user_name}! Have a great day.")
        break
        
    # 📜 FEATURE: HELP MENU
    elif user_input == "Help":
        print("\n--- 🛠️ Utility Commands ---")
        print("💡 'Time'   - Show current date and time")
        print("💡 'Calc'   - Open the math calculator")
        print("💡 'Todo'   - Manage your daily task list")
        print("💡 'Timer'  - Set a quick countdown alert")
        print("💡 'System' - View bot technical details")
        print("\n--- 🎮 Fun Commands ---")
        print("💡 'Flip'   - Flip a coin / 'Roll' - Roll a die")
        print("💡 'Rps'    - Play Rock, Paper, Scissors")
        print("💡 'Name'   - Change your name")
        print("💡 'Exit'   - Close the bot")
        print("-" * 30)

    # ⏰ FEATURE 1: DATE & TIME
    elif user_input == "Time":
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        current_date = now.strftime("%B %d, %Y (%A)")
        print(f"Dex: 📅 Today is {current_date}")
        print(f"Dex: ⏰ The current time is {current_time}")
        print("-" * 30)

    # 🧮 FEATURE 2: CALCULATOR
    elif user_input == "Calc":
        print("Dex: Math mode activated. Enter two numbers and an operator.")
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ").strip()
            num2 = float(input("Enter second number: "))
            
            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                result = num1 / num2 if num2 != 0 else "Error (Cannot divide by zero!)"
            else:
                result = "Invalid Operator"
                
            print(f"Dex: 📊 Result: {result}")
        except ValueError:
            print("Dex: ⚠️ Please enter valid numbers!")
        print("-" * 30)

    # 📝 FEATURE 3: TODO LIST
    elif user_input == "Todo":
        print("\n--- 📝 Your Todo List ---")
        if not todo_list:
            print("[Your list is currently empty]")
        else:
            for index, task in enumerate(todo_list, 1):
                print(f"{index}. {task}")
        print("------------------------")
        
        action = input("Type 'add' to add, 'remove' to delete, or press Enter to skip: ").strip().lower()
        if action == "add":
            new_task = input("What task do you want to add? ").strip()
            if new_task:
                todo_list.append(new_task)
                print(f"Dex: ✅ Added '{new_task}' to your list!")
        elif action == "remove":
            try:
                task_num = int(input("Enter the task number to delete: "))
                removed = todo_list.pop(task_num - 1)
                print(f"Dex: ❌ Removed '{removed}' from your list.")
            except (ValueError, IndexError):
                print("Dex: ⚠️ Invalid task number.")
        print("-" * 30)

    # ⏳ FEATURE 4: TIMER
    elif user_input == "Timer":
        try:
            seconds = int(input("How many seconds should I count down? "))
            print(f"Dex: Starting timer for {seconds} seconds...")
            time.sleep(seconds)
            print("Dex: 🚨 BEEP BEEP BEEP! Time is up!")
        except ValueError:
            print("Dex: ⚠️ Please enter a whole number of seconds.")
        print("-" * 30)

    # ⚙️ FEATURE 5: SYSTEM INFO
    elif user_input == "System":
        print(f"Dex: 🏷️ Bot Name: Dex")
        print(f"Dex: 🚀 Version: {VERSION}")
        print(f"Dex: 🐍 Language: Python 3")
        print(f"Dex: 📂 Total chat intents loaded: {len(chat_data)}")
        print("-" * 30)

    # 🪙 COIN FLIPPER
    elif user_input == "Flip":
        result = random.choice(["🪙 HEADS!", "🪙 TAILS!"])
        print(f"Dex: Flipping a coin... It landed on: {result}")
        print("-" * 30)

    # 🎲 DICE ROLLER
    elif user_input == "Roll":
        dice_number = random.randint(1, 6)
        print(f"Dex: 🎲 You rolled a: {dice_number}")
        print("-" * 30)

    # ✊✋✌️ ROCK, PAPER, SCISSORS
    elif user_input == "Rps":
        player_choice = input("Choose Rock, Paper, or Scissors: ").strip().capitalize()
        if player_choice in ["Rock", "Paper", "Scissors"]:
            bot_choice = random.choice(["Rock", "Paper", "Scissors"])
            print(f"Dex chose: {bot_choice}")
            if player_choice == bot_choice:
                print("Dex: 👔 It's a tie!")
            elif (player_choice == "Rock" and bot_choice == "Scissors") or \
                 (player_choice == "Paper" and bot_choice == "Rock") or \
                 (player_choice == "Scissors" and bot_choice == "Paper"):
                print("Dex: 🎉 You win!")
            else:
                print("Dex: 🤖 I win!")
        else:
            print("Dex: ⚠️ Invalid choice!")
        print("-" * 30)

    # 🏷️ NAME CUSTOMIZER
    elif user_input == "Name":
        new_name = input("What should I call you? ").strip()
        if new_name:
            user_name = new_name
            print(f"Dex: Awesome, nice to meet you, {user_name}!")
        print("-" * 30)
    
    # 💬 DICTIONARY CHAT CHECKER
    else:
        found_answer = False
        for key in chat_data:
            if key in user_input:
                bot_reply = random.choice(chat_data[key])
                print(f"Dex: {bot_reply}")
                found_answer = True
                break
        
        if not found_answer:
            print("Dex: I don't know that command yet. Try typing 'Help' to see what I can do!")
