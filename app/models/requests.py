from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from user import RegularUser
    from responses import ModelResult, TransactionResult
    #from responses import ModelResult, TransactionResult

class Request(SQLModel, table = False): 
    #__tablename__='requests'# не забыть убрать     
    id: Optional[int] = Field(default=None, primary_key = True)
    created_time: datetime = Field(default_factory=datetime.now)
    status: str = Field(default="pending")  # pending, processing, completed, failed
    

class ModelRequest(Request, table=True):
    __tablename__ = "model_requests"

    id: Optional[int] = Field(default=None, primary_key = True)
    input_data: str = Field(default="")

    user_id: int = Field(foreign_key="regular_users.id")
    regular_user: "RegularUser" = Relationship(back_populates="model_requests") 

    response: Optional["ModelResult"] = Relationship(
        back_populates="request",
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"}
    )


class TransactionRequest(Request, table=True):
    __tablename__ = "transaction_requests"

    id: Optional[int] = Field(default=None, primary_key = True)
    #amount: Decimal = Field(default=Decimal('0.0'), sa_column=Column(Numeric(15, 2)))
    transaction_type: str = Field()  # Тип транзакции ('deposit', 'withdrawal')

    user_id: int = Field(foreign_key="regular_users.id")
    regular_user: "RegularUser" = Relationship(back_populates="transaction_requests") 

    response: Optional["TransactionResult"] = Relationship(
        back_populates="request",
        sa_relationship_kwargs={"uselist": False, "cascade": "all, delete-orphan"}
    )