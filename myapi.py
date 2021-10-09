from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

users = {
    1: {
        "name" : "dipo",
        "age": 20,
        "class": "year 2021"
    }
}

class User(BaseModel):
    name: str
    age: int
    year: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def home():
	return {"name": 'First Data'}

@app.get("/get-user/{user_id}")
def get_user(user_id: int=Path(None, description="id of the user")):
    return users[user_id]

@app.get("/get-by-name")
def get_user(*, name: Optional[str] =None, test:int):
    for user_id in users:
        if users[user_id]["name"] == name:
            return users[user_id]
        return {"data not found"}

@app.post("/create-user/")
def create_user(user_id:int, user: User):
    if user_id in users:
        return{"user exists"}
    
    users[user_id] = user
    return users[user_id]

@app.put("/update-user/{user_id}")
def update_user(user_id:int, user: UpdateUser):
    if user_id not in users:
        return {"user doesnt exist"}

    if user.name!= None:
        users[user_id].name = user.name

    if user.age!= None:
        users[user_id].age = user.age

    if user.year!= None:
        users[user_id].name = user.year     
    
    return users[user_id]