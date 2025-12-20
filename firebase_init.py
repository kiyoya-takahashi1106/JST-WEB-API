import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("./jst-robot-project-firebase-adminsdk-fbsvc-78ad96de21.json")
firebase_admin.initialize_app(cred)