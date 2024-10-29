from users import create_user, sign_in_user, sign_out_user, update_user, delete_user
from transactions import add_transaction, update_transaction, delete_transaction, get_transactions
from database import db

def main():
    user_id = None

    # User login or sign-up process
    while not user_id:
        print("\nWelcome to the Personal Finance Manager")
        choice = input("Do you have an account? (yes/no): ").strip().lower()

        # Sign in if the user has an account
        if choice == "yes":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user_id = sign_in_user(email, password)
            
        # Create an account if the user doesn't have one
        elif choice == "no":
            email = input("Enter your email to create an account: ")
            password = input("Enter your password: ")
            name = input("Enter your name: ")
            lastname = input("Enter your lastname: ")
            create_user(email, password, name, lastname)
            user_id = sign_in_user(email, password)
            
        # Prompt for valid input
        else:
            print("Please answer with 'yes' or 'no'.")

    # After login, display user info and show menu
    if user_id:
         # Retrieve and display the logged-in user's information
        user_ref = db.collection('Users').document(user_id)
        user_data = user_ref.get().to_dict()
        print(f"Welcome {user_data['name']} {user_data['lastname']}!")
        print("------------------")
        print("Login successful.")
        show_menu(user_id)

def show_menu(user_id):
    # Display the main menu and handle user selections
    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Update User")
        print("6. Delete User")
        print("7. Sign Out")
        print("8. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            transaction_id = input("Enter transaction ID: ")
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter transaction type (income/expense): ")
            add_transaction(transaction_id, user_id, amount, transaction_type)
        elif choice == '2':
            get_transactions(user_id)
        elif choice == '3':
            transaction_id = input("Enter transaction ID to update: ")
            amount = input("Enter new amount (leave blank to keep current): ")
            transaction_type = input("Enter new transaction type (leave blank to keep current): ")
            update_transaction(transaction_id, float(amount) if amount else None, transaction_type if transaction_type else None)
        elif choice == '4':
            transaction_id = input("Enter transaction ID to delete: ")
            delete_transaction(transaction_id)
        elif choice == '5':
            email = input("Enter new email (leave blank to skip): ")
            name = input("Enter new name (leave blank to skip): ")
            lastname = input("Enter new lastname (leave blank to skip): ")
            update_user(user_id, name=name if name else None, lastname=lastname if lastname else None, email=email if email else None)
        elif choice == '6':
            delete_user(user_id)
            print("User deleted. Exiting...")
            break
        elif choice == '7':
            sign_out_user(user_id)
            print("Signed out successfully.")
            break
        elif choice == '8':
            # Exit the application
            print("Exiting...")
            break
        else:
             # Handle invalid menu selections
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
