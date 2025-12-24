from fastapi import FastAPI

import firebase_init
from firebase_admin import firestore

from datetime import datetime

from schemas import ReservationRequest


app = FastAPI()
db = firestore.client()


# test
@app.get("/")
def root():
    return {"message": "Hello FastAPI"}

@app.get("/save")
def save_data():
    data = {
        "message": "hello firestore",
        "time": datetime.utcnow().isoformat()
    }
    db.collection("test").add(data)
    return {
        "status": "saved",
        "data": data
    }


# reservation
@app.post("/reservation")
def reserve(request: ReservationRequest):
    data = request.model_dump()
    data["created_at"] = datetime.utcnow().isoformat()

    post_ref = db.collection("posts").add(data)

    return {
        "success": True,
        "sensitive": False,
        "post_id": post_ref[1].id
    }


# get posts
@app.get("/posts")
def get_all_posts():
    posts_ref = db.collection("posts")
    docs = posts_ref.stream()

    posts = []
    for doc in docs:
        post = doc.to_dict()
        post["id"] = doc.id
        posts.append(post)

    return {
        "success": True,
        "posts": posts
    }