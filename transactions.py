from database import db

def add_transaction(transaction_id, user_id, amount, transaction_type):
    # Prepare transaction data for a new transaction
    transaction_data = {
        "user_id": user_id,
        "amount": amount,
        "type": transaction_type
    }
     # Add the transaction data to the 'Transactions' collection with the specified transaction ID
    db.collection('Transactions').document(transaction_id).set(transaction_data)
    print(f"Transaction of {transaction_type} for ${amount} added with ID: {transaction_id}")

def update_transaction(transaction_id, amount=None, transaction_type=None):
    # Reference the transaction document by transaction ID
    transaction_ref = db.collection('Transactions').document(transaction_id)

    # Update the transaction amount if a new amount is provided
    if amount:
        transaction_ref.update({"amount": amount})

    # Update the transaction type if a new type is provided
    if transaction_type:
        transaction_ref.update({"type": transaction_type})
    print(f"Transaction {transaction_id} updated.")

def delete_transaction(transaction_id):
     # Delete the transaction document from the 'Transactions' collection
    db.collection('Transactions').document(transaction_id).delete()
    print(f"Transaction {transaction_id} deleted.")

def get_transactions(user_id):
    # Query for all transactions associated with the specified user ID
    transactions_ref = db.collection('Transactions').where("user_id", "==", user_id)

    # Retrieve and print each transaction in the query result
    transactions = transactions_ref.stream()
    transactions_list = list(transactions) 
    if not transactions_list:
        print("No transactions registered.")
    else:
        for transaction in transactions_list:
            print(transaction.id, transaction.to_dict())
