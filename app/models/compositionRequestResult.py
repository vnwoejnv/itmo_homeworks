#тк пользователь может выполнить как запрос для пололнения баланса, так и запрос к модели
#удобно описать некотоыре общие свойства запроса тут 
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Request(SQLModel, table=True):
    __tablename__ = "requests"

    id: Optional[int] = Field(default=None, primary_key = True)
    created_time: datetime = Field(default_factory=datetime.now)
    status: str = Field(default="pending")  # pending, processing, completed, failed

    result: Optional["Result"] = Relationship(
        back_populates="request",
        sa_relationship_kwargs={"uselist": False}
    )


    type: str = Field(default="base_request")
    __mapper_args__ = {
        "polymorphic_identity": "request",
        "polymorphic_on": "type"
    }

    


class Result(SQLModel, table=True):
    __tablename__ = "results"

    id: Optional[int] = Field(default=None, primary_key = True)
    request_id: int = Field(foreign_key="requests.id")
    completion_time: datetime = Field(default_factory=datetime.now)

    request: "Request" = Relationship(
        back_populates="result",
        sa_relationship_kwargs={
            "foreign_keys": [request_id],
            "uselist": False
        }
        )   


    type: str = Field(default="base_result")
    __mapper_args__ = {
        "polymorphic_identity": "result",
        "polymorphic_on": "type"
    }
