from compositionRequestResult import Request, Result
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, Dict, Any, List
from datetime import datetime
from decimal import Decimal
from sqlalchemy.dialects.postgresql import JSONB


class TransactionRequest(Request, table=True):
    __tablename__ = "transaction_requests"
    
    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        foreign_key="requests.id"
    )
    
    user_id: int = Field(foreign_key="regular_users.id")
    amount: Decimal = Field(default=Decimal('0.0'))
    transaction_type: str = Field()  # 'deposit', 'withdrawal'
    
    # Связь с пользователем
    regular_user: "RegularUser" = Relationship(back_populates="transactions")
    
    __mapper_args__ = {
        "polymorphic_identity": "transaction_request",
    }


class TransactionResult(Result, table=True):
    __tablename__ = "transaction_results"
    
    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        foreign_key="results.id"
    )
    
    approved: bool = Field(default=False)
    admin_id: Optional[int] = Field(default=None, foreign_key="admin_users.id")
    notes: Optional[str] = Field(default=None)
    
    admin: Optional["AdminUser"] = Relationship(
        back_populates="transaction_results",
        sa_relationship_kwargs={"uselist": False}  
    )
    
    __mapper_args__ = {
        "polymorphic_identity": "transaction_result",
    }

