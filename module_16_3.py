from fastapi import FastAPI
from typing import Dict

# Создаем объект FastAPI
app = FastAPI()

# Инициализируем словарь users с начальным значением
users: Dict[str, str] = {'1': 'Имя: Example, возраст: 18'}

# GET запрос для получения всех пользователей
@app.get("/users")
def get_users():
    return users

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}")
def add_user(username: str, age: int):
    # Находим максимальный ключ в словаре и добавляем новый пользователь с ключом на 1 больше
    new_id = str(max(map(int, users.keys())) + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {new_id} is registered"}

# PUT запрос для обновления данных пользователя
@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id in users:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return {"message": f"User {user_id} has been updated"}
    else:
        return {"message": f"User {user_id} not found"}

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id in users:
        del users[user_id]
        return {"message": f"User {user_id} has been deleted"}
    else:
        return {"message": f"User {user_id} not found"}
