import platform
import threading
import subprocess
import time

#  ▗▄▖▗▄▄▄▖▗▄▄▖  ▗▄▄▖
# ▐▌ ▐▌ █  ▐▌ ▐▌▐▌   
# ▐▛▀▜▌ █  ▐▛▀▚▖ ▝▀▚▖
# ▐▌ ▐▌ █  ▐▙▄▞▘▗▄▄▞

def sendtoes(title, message):
    subprocess.run(['notify-send', title, message])

def background_reminder(delay, msg):
    time.sleep(delay)
    sendtoes("Reminder Alert!", msg)

operatingsystem = [platform.system(), platform.release(), platform.version()]

commandlist = ["help", "exit", "calculator", "reminder",]

print(f"Operating System: {operatingsystem[0]} {operatingsystem[1]} {operatingsystem[2]}")

print("Hello, Welcome to 'Automate The Boring Stuff' or 'ATBS' for short!")

print("NOTE: enter help to get the full list of available commands.")

while True:
    command = input("Enter a command: ")
    if command == "help":
        print("Available commands:")
        for cmd in commandlist:
            print(f"- {cmd}")
    elif command == "exit":
        print("Exiting the program.")
        break
    elif command == "calculator":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operation (+, -, *, /): ")
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2
        else:
            print("Invalid operation.")
            continue
        print(f"Result: {result}")
    elif command == "reminder":
        try:
            message = input("Enter the reminder message: ")
            timetoremind = int(input("Enter the time in seconds for the reminder: "))

            reminder_thread = threading.Thread(
                target=background_reminder, 
                args=(timetoremind, message),
                daemon=True
            )
            reminder_thread.start()
            
            print(f"Success: Reminder set for {timetoremind} seconds from now!")
        except ValueError:
            print("Invalid input. Please enter a valid number for the time.")
    else:
        print(f"Unknown command: {command}. Type 'help' to see the list of available commands.")