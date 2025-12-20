from fastapi import FastAPI

import firebase_init
from firebase_admin import firestore

from datetime import datetime


app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/save")
def save_data():
    db = firestore.client()
    data = {
        "message": "hello firestore",
        "time": datetime.utcnow().isoformat()
    }
    db.collection("test").add(data)
    return {
        "status": "saved",
        "data": data
    }