import platform
operatingsystem = [platform.system(), platform.release(), platform.version()]
commandlist = ["help", "exit", "calculator - placeholder for now", "reminder - placeholder for now"]
print(f"Operating System: {operatingsystem[0]} {operatingsystem[1]} {operatingsystem[2]}")
print("Hello, Welcome to 'Automate The Boring Stuff' or 'ATBS' for short!")
print("NOTE: enter help to get the full list of available commands.")
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