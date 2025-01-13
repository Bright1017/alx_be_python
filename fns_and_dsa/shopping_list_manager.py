def main():
    shopping_list = []

    def display_menu():
        print("\nShopping List Manager")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View the list")
        print("4. Exit")

    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))

            if choice == 1:
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"'{item}' has been added to the list.")
                else:
                    print("Item cannot be empty.")

            elif choice == 2:
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from the list.")
                else:
                    print(f"'{item}' is not in the shopping list.")

            elif choice == 3:
                if shopping_list:
                    print("\nCurrent Shopping List:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")
                else:
                    print("The shopping list is empty.")

            elif choice == 4:
                print("Exiting the Shopping List Manager. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
