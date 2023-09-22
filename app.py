from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID

app = FastAPI()

db: List[User] = [
  User( 
    id = UUID("b7e581b0-f389-4945-9da6-b3cde469e488"),
    first_name = "Ana",
    last_name = "Lobato",
    email = "email@gmail.com",
    role= [Role.role_1]
  ),
  User( 
    id = UUID("02d78dea-ad98-4a14-8ef2-9b3e38165f84"),
    first_name = "Hévelin",
    last_name = "Lima",
    email = "email@gmail.com",
    role= [Role.role_2]
  ),
  User( 
    id = UUID("d4af3d86-1beb-49ed-b8eb-41340fa7476a"),
    first_name = "Cynthia",
    last_name = "Zanoni",
    email = "email@gmail.com",
    role= [Role.role_3]
  )
]

@app.get("/")
async def root():
  return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
  return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
  for user in db:
    if user.id == id:
      return user
  return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
  for user in db:
    if user.id == id:
      db.remove(user)
      return
  raise HTTPException(
    status_code= 404,
    detail= f"Usuário com o id: {id} não encontrado."
  )