# app/main.py

from fastapi import FastAPI
from app.transactions import send_money

app = FastAPI()

@app.get("/transfer/")
def transfer(sender:str, receiver:str, amount:float):
    return {
        "message": send_money(sender, receiver, amount)
    }