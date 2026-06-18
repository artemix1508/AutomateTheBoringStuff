print("Hello, Welcome to 'Automate The Boring Stuff' or 'ATBS' for short!")
print("NOTE: enter help to get the full list of available commands.")
commandlist = ["help", "exit", "calculator", "reminder"]
#To do: add more FUNCTIONING commands cuz i only have 2 working commands right now, and the rest are just placeholders for now.
while True:
    command = input("Enter a command: ")
    if command == "help":
        print("Available commands:")
        for cmd in commandlist:
            print(f"- {cmd}")
    elif command == "exit":
        print("Exiting the program.")
        break
    else:
        print(f"Unknown command: {command}. Type 'help' to see the list of available commands.")