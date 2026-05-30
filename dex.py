from datetime import datetime
import math
import random

# 🏗️ THE BOT BLUEPRINT (Class)
class AssistantBot:
    def __init__(self, name, version):
        # Object Properties (The bot's local memory bank)
        self.name = name
        self.version = version
        self.user_name = "User"
        self.todo_list = []  # 📋 Empty box to hold your tasks
        self.chat_data = {
            "Hello": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
            "Hi": ["Hey there!", "Hi! Ready to chat?", "Hello!"],
            "Good": ["That's awesome! I'm happy to hear that.", "Sweet! Good vibes only."],
            "Sad": ["I'm sorry to hear that. Sending a virtual hug! 🤗", "Cheer up! You got this!"],
            "Tired": ["Go get some rest! 😴", "Take a break, coding can wait."]
        }

    # 🚪 SKILL: Welcome Greeting (Our simple "Login" alternative)
    def boot_up(self):
        print(f"🤖 {self.name}: Assistant Bot Activated! [{self.version}]")
        name_input = input(f"{self.name}: Before we begin, what is your name? ").strip()
        if name_input:
            # Capitalize just the first letter cleanly
            self.user_name = name_input[0].upper() + name_input[1:] if len(name_input) > 0 else name_input
        print(f"\nWelcome back, {self.user_name}! Type 'Help' to see what I can do.")
        print("=" * 60)

    # ⏰ SKILL: Show Date & Time
    def show_time(self):
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        current_date = now.strftime("%B %d, %Y (%A)")
        print(f"{self.name}: 📅 Today is {current_date}")
        print(f"{self.name}: ⏰ The current time is {current_time}")
        print("-" * 30)

    # ⚙️ SKILL: Show System Info
    def show_system_info(self):
        print(f"{self.name}: 🏷️ Bot Name: {self.name}")
        print(f"{self.name}: 🚀 Version: {self.version}")
        print(f"{self.name}: 🐍 Language: Python 3")
        print(f"{self.name}: 📂 Total chat intents loaded: {len(self.chat_data)}")
        print("-" * 30)

    # 🪙 SKILL: Coin Flipper
    def flip_coin(self):
        result = random.choice(["🪙 HEADS!", "🪙 TAILS!"])
        print(f"{self.name}: Flipping a coin... It landed on: {result}")
        print("-" * 30)

    # 🎲 SKILL: Dice Roller
    def roll_die(self):
        dice_number = random.randint(1, 6)
        print(f"{self.name}: 🎲 You rolled a: {dice_number}")
        print("-" * 30)

    # 📋 SKILL: Add a Task to Todo List
    def add_todo(self):
        task = input("Enter the task/chore to add: ").strip()
        if task:
            self.todo_list.append(task)
            print(f"{self.name}: Added '{task}' to your todo list!")
        else:
            print(f"{self.name}: Task cannot be empty!")
        print("-" * 30)

    # 📜 SKILL: View All Todo Tasks
    def show_todo(self):
        print(f"\n--- 📋 {self.user_name}'s Todo List ---")
        if not self.todo_list:
            print("Your list is completely empty! Great job.")
        else:
            for index, task in enumerate(self.todo_list, start=1):
                print(f"{index}. [ ] {task}")
        print("-" * 30)

    # 🧮 SKILL: Advanced Calculator (Safely packed inside its own function)
    def calculate(self):
        print("\n--- 🧮 Dex Advanced Calculator ---")
        print("Operations: + , - , * , / , square , sqrt , sin , cos , tan")
        op = input("Choose an operation: ").strip().lower()

        # Single number math operations
        if op in ["square", "sqrt", "sin", "cos", "tan"]:
            try:
                num = float(input("Enter number: "))
                if op == "square":
                    print(f"Result: {num}² = {num ** 2}")
                elif op == "sqrt":
                    print(f"Result: √{num} = {math.sqrt(num)}")
                elif op == "sin":
                    print(f"Result: sin({num}) = {math.sin(math.radians(num))}")
                elif op == "cos":
                    print(f"Result: cos({num}) = {math.cos(math.radians(num))}")
                elif op == "tan":
                    print(f"Result: tan({num}) = {math.tan(math.radians(num))}")
            except ValueError:
                print("❌ Error: Invalid number entered!")
            except Exception as e:
                print(f"❌ Error: {e}")

        # Double number math operations
        elif op in ["+", "-", "*", "/"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if op == "+":
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif op == "-":
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif op == "*":
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif op == "/":
                    if num2 == 0:
                        print("❌ Error: Cannot divide by zero!")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("❌ Error: Invalid numbers entered!")
        else:
            print("❌ Unknown calculation operation!")
        print("-" * 30)

    # 💬 SKILL: Smart Conversational Matcher
    def handle_chat(self, user_input):
        # We clean the input completely for matching: strip spacing and make it lowercase
        clean_input = user_input.strip().lower()
        
        found_answer = False
        for key in self.chat_data:
            # Match safely even if the user typed mixed casing like "hI dEx"
            if key.lower() in clean_input:
                bot_reply = random.choice(self.chat_data[key])
                print(f"{self.name}: {bot_reply}")
                found_answer = True
                break
        
        if not found_answer:
            print(f"{self.name}: I don't know that command yet. Type 'Help' to check available keywords!")


# ==========================================
# 🚀 EXECUTION CODE
# ==========================================

# Create the object instance
dex = AssistantBot("Dex", "v2.7.5")

# Run the boot greeting once at startup
dex.boot_up()

# The clean, streamlined main application loop
while True:
    raw_input = input(f"\n[Chat] {dex.user_name} 👤: ").strip()
    
    if not raw_input:
        continue
        
    # Standardize phrasing format for main structural words
    user_input = raw_input[0].upper() + raw_input[1:] if len(raw_input) > 0 else raw_input
    
    if user_input == "Exit":
        print(f"\n{dex.name}: Goodbye {dex.user_name}! Have a fantastic day.")
        break
        
    elif user_input == "Help":
        print("\n--- 🛠️ Utility Commands ---")
        print("💡 'Time'   - Show current date and time")
        print("💡 'System' - View bot technical details")
        print("💡 'Calc'   - Open the Advanced Calculator")
        print("\n--- 📋 Task List Commands ---")
        print("💡 'Todo'   - Add a new task to your list")
        print("💡 'Tasks'  - View all saved tasks")
        print("\n--- 🎮 Fun Commands ---")
        print("💡 'Flip'   - Flip a coin")
        print("💡 'Roll'   - Roll a die")
        print("💡 'Exit'   - Close the bot")
        print("-" * 30)

    # Triggering object actions cleanly from our simple if/elif router
    elif user_input == "Time":
        dex.show_time()

    elif user_input == "System":
        dex.show_system_info()

    elif user_input == "Calc":
        dex.calculate()

    elif user_input == "Todo":
        dex.add_todo()

    elif user_input == "Tasks":
        dex.show_todo()

    elif user_input == "Flip":
        dex.flip_coin()

    elif user_input == "Roll":
        dex.roll_die()
    
    else:
        # Pass unknown keywords down to the chat engine to see if they match greetings
        dex.handle_chat(raw_input)