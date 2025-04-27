from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int
    

database = {
    1: User(id=1, name="John", email="john@example.com", age=30),
    2: User(id=2, name="Jane", email="jane@example.com", age=25),
    3: User(id=3, name="Bob", email="bob@example.com", age=35),
    4: User(id=4, name="Alice", email="alice@example.com", age=40),
}


@app.post("/users")
def create_user(user: User):
    if user.id in database:
        return {"error": "Usuario ya existe"}
    database[user.id] = user
    return {"message": "Usuario creado correctamente"}

@app.get("/users")
def get_users():
    return list(database.values())

@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = database.get(user_id)
    if user:
        return user
    return {"error": "Usuario no encontrado"}

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in database:
        return {"error": "Usuario no encontrado"}
    database[user_id] = user
    return {"message": "Usuario actualizado correctamente"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in database:
        return {"error": "Usuario no encontrado"}
    del database[user_id]
    return {"message": "Usuario eliminado correctamente"}