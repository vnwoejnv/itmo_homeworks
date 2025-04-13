from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from models.requests import ModelRequest, TransactionRequest

class Result(SQLModel):
    completion_time: datetime = Field(default_factory=datetime.now)


class ModelResult(Result, table=True):
    __tablename__ = "model_results"
    id: Optional[int] = Field(default=None, primary_key=True)
    output_data: str = Field(default="")
    #credits_spent: Decimal = Field(default=Decimal('0.0'))

    request_id: int = Field(foreign_key="model_requests.id", unique=True)
    request: "ModelRequest" = Relationship(back_populates="response") 


class TransactionResult(Result, table=True):
    __tablename__ = "transaction_results"
    id: Optional[int] = Field(default=None, primary_key=True)
    approved: bool = Field(default=False)
    notes: Optional[str] = Field(default=None)

    request_id: int = Field(foreign_key="transaction_requests.id", unique=True)
    request: "TransactionRequest" = Relationship(back_populates="response")