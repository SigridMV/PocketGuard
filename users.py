from database import db

def add_user(email, password, name, lastname):
    # Add a new user with provided data
    user_data = {
        "email": email,
        "password": password,
        "name": name,
        "lastname": lastname
    }
    db.collection("Users").add(user_data)
    print("User added.")

def create_user(email, password, name, lastname):
    # Create a user by calling add_user function
    add_user(email, password, name, lastname)
    print(f"User created: {email}")

def sign_in_user(email, password):
     # Authenticate user by checking email and password
    users_ref = db.collection('Users').where("email", "==", email).stream()
    for user in users_ref:
        if user.to_dict()['password'] == password:
            print("-----------------------")
            print(f"User {email} signed in.")
            return user.id # Return user ID on successful sign-in
    print("Invalid credentials.")
    return None # Return None if authentication fails

def update_user(user_id, name=None, lastname=None, email=None):
    # Update user information if new values are provided
    user_ref = db.collection('Users').document(user_id)
    if name:
        user_ref.update({"name": name})
    if lastname:
        user_ref.update({"lastname": lastname})
    if email:
        user_ref.update({"email": email})
    print(f"User {user_id} updated.")

def delete_user(user_id):
    # Delete a user by user ID
    db.collection('Users').document(user_id).delete()
    print(f"User {user_id} deleted.")

def get_user(user_id):
     # Retrieve and display a user's details by user ID
    user_ref = db.collection('Users').document(user_id)
    user = user_ref.get()
    if user.exists:
        print(user.to_dict())
    else:
        print(f"User {user_id} not found.")

def watch_users():
     # Set up a real-time listener for changes in the 'Users' collection
    users_ref = db.collection('Users')

    def on_snapshot(snapshot, changes, read_time):
        # Handle real-time updates for added, modified, or removed users
        for change in changes:
            if change.type.name == 'ADDED':
                print(f"New user: {change.document.id} => {change.document.to_dict()}")
            elif change.type.name == 'MODIFIED':
                print(f"User modified: {change.document.id} => {change.document.to_dict()}")
            elif change.type.name == 'REMOVED':
                print(f"User deleted: {change.document.id}")
    # Start listening to changes in the 'Users' collection          
    users_watch = users_ref.on_snapshot(on_snapshot)
