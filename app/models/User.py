from decimal import Decimal
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import Column, ForeignKey, Integer

if TYPE_CHECKING:
    from models.requests import ModelRequest, TransactionRequest

class User(SQLModel):
    username: str = Field(index=True)
    email: str = Field(index=True)   
    password_hash: str = Field() 
 

class RegularUser(User, table=True):
    __tablename__='regular_users'

    id: Optional[int] = Field(default=None, primary_key=True)
    #balance: Decimal = Field(default=Decimal('0.00'), sa_type="NUMERIC(15, 2)")
    model_requests: List["ModelRequest"] = Relationship(
        back_populates="regular_user",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
        )
    transaction_requests: List["TransactionRequest"] = Relationship(
        back_populates="regular_user",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"}
        )
    
    def __str__(self):
        return f"RegularUser(id={self.id}, username={self.username}, email={self.email})"
    def __repr__(self):
        return f"RegularUser(id={self.id}, username={self.username}, email={self.email})"
                            


# class AdminUser(User, table=True):
#     __tablename__ = 'admin_users'
#     id: Optional[int] = Field(default=None, primary_key=True)
#     #может быть нужны будут еще поля 
#     #transaction_results: List["TransactionResult"] = Relationship(
#     #     back_populates="admin",
#     #     sa_relationship_kwargs={"cascade": "save-update"}
#     #)