# app/main.py

from fastapi import FastAPI
from app.transactions import send_money,deposit_money

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Kigula Senders"
    }

@app.get("/transfer/")
def transfer(sender:str, receiver:str, amount:float):
    return {
        "message": send_money(sender, receiver, amount)
    }

@app.get("/deposit/")
def deposit(depositor:str, amount:float):
    return {
        "message": deposit_money(depositor, amount)
    }