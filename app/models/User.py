from decimal import Decimal
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from sqlmodel import SQLModel, Field, Relationship

class User(SQLModel, table=True):

    __tablename__ = "users"

    id: Optional[int] = Field(default=None, primary_key = True)
    username: Optional[str] = Field(index=True, nullable=False)
    email: Optional[str] = Field(index=True, nullable=False)
    password_hash: Optional[str] = Field(nullable=False)

    type: str = Field(default="user")

    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": "type"
    }
    


class RegularUser(User, table=True):
    __tablename__ = "regular_users"

    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        foreign_key="users.id"
    )

    balance: Decimal = Field(default=0, sa_type="NUMERIC(15, 2)")
    last_transaction_id: Optional[int] = Field(foreign_key="transactions.id")

    model_requests: List["ModelRequest"] = Relationship(back_populates="regular_user")
    transactions: List["Transaction"] = Relationship(back_populates="regular_user")

    
    __mapper_args__ = { 
        "polymorphic_identity": "regular_user", 
    }

class AdminUser(User, table=True): #наследуется от User
    __tablename__ = "admin_users"

    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        foreign_key="users.id"
    )
    # можно добавить поля с правами администратора

    transaction_results: List["TransactionResult"] = Relationship(
    back_populates="admin"
)

    __mapper_args__ = {
        "polymorphic_identity": "admin_user", 
    }
        
    