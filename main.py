from fastapi import FastAPI, HTTPException
from schemas import AccountCreate, Transaction
from services import BankService

app = FastAPI(title="Simple Bank API")
bank_service = BankService()

@app.post("/accounts/")
def create_account(account: AccountCreate):
    return bank_service.create_account(account)

@app.get("/accounts/{account_id}")
def get_balance(account_id: str):
    return bank_service.get_account_balance(account_id)

@app.post("/accounts/{account_id}/deposit")
def deposit(account_id: str, transaction: Transaction):
    return bank_service.deposit(account_id, transaction.amount)

@app.post("/accounts/{account_id}/withdraw")
def withdraw(account_id: str, transaction: Transaction):
    return bank_service.withdraw(account_id, transaction.amount)
