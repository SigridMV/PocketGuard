from users import create_user, sign_in_user, update_user, delete_user, get_user
from transactions import add_transaction, get_transactions
from database import db

def main():
    user_id = None
    
    # User login or account creation loop
    while not user_id:
        print()
        print("Welcome to the Personal Finance Manager")
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
        
        # Prompt for valid input if response is unclear
        else:
            print("Please answer with 'yes' or 'no'.")

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
        print("3. Update User")
        print("4. Delete User")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            # Add a new transaction
            transaction_id = input("Enter transaction ID: ")
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter transaction type (income/expense): ")
            add_transaction(transaction_id, user_id, amount, transaction_type)
        # Retrieve and display transactions for the user
        elif choice == '2':
            get_transactions(user_id)
        elif choice == '3':
         # Update user's email address
            email = input("Enter new email (leave blank to skip): ")
            update_user(user_id, email=email if email else None)
        elif choice == '4':
            # Delete the user's account and exit the loop
            delete_user(user_id)
            print("User deleted. Exiting...")
            break
        elif choice == '5':
            # Exit the application
            print("Exiting...")
            break
        else:
             # Handle invalid menu selections
            print("Invalid option, please try again.")

# Run the main function
if __name__ == "__main__":
    main()