from pydantic import BaseModel

class BankAccountBase(BaseModel):
    owner: str

class BankAccountCreate(BankAccountBase):
    balance: int

class BankAccount(BankAccountBase):
    id: int
    balance: int

    class Config:
        orm_mode = True
