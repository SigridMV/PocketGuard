import firebase_admin 
from firebase_admin import credentials, firestore
import os
import warnings

# Ignore specific warnings from Firestore's base collection module
warnings.filterwarnings("ignore", category=UserWarning, module="google.cloud.firestore_v1.base_collection")

def initialize_firestore():
     # Set the environment variable for Firebase credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebase_credentials.json"

    # Use default application credentials for Firebase authentication
    cred = credentials.ApplicationDefault()

      # Initialize the Firebase app with the project ID
    firebase_admin.initialize_app(cred, {
        'projectId': 'pocketguard-54fb2',
    })
    # Return a Firestore client for interacting with the database
    return firestore.client()

# Initialize the Firestore database instance
db = initialize_firestore()
