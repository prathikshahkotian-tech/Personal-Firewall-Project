print("===================================")
print("     Personal Firewall System      ")
print("===================================")

while True:
    print("\nMenu")
    print("1. Block an IP Address")
    print("2. Allow an IP Address")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        ip = input("Enter IP Address to block: ")
        print(f"{ip} has been blocked successfully.")

    elif choice == "2":
        ip = input("Enter IP Address to allow: ")
        print(f"{ip} has been allowed successfully.")

    elif choice == "3":
        print("Exiting Personal Firewall...")
        break

    else:
        print("Invalid choice. Please try again.")
