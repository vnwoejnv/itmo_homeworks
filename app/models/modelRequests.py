from datetime import datetime
from decimal import Decimal
from typing import Dict, List, Tuple, Optional, Any
from sqlmodel import SQLModel, Field, Relationship
from compositionRequestResult import Request, Result
from sqlalchemy.dialects.postgresql import JSONB


class ModelRequest(Request, table = True): 
    __tablename__ = "model_requests"
    
    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        foreign_key="requests.id"
    )
    user_id: int = Field(foreign_key="regular_users.id")
    regular_user: "RegularUser" = Relationship(back_populates="model_requests")

    input_data: Dict[str, Any] = Field(sa_type=JSONB)

    __mapper_args__ = { 
        "polymorphic_identity": "model_request", 
    }
    


class ModelResponse(Result, table=True):  
    __tablename__ = "model_responses"

    id: Optional[int] = Field(
        default=None, 
        primary_key=True,
        foreign_key="results.id"
    )
    
    output_data: Dict[str, Any] = Field(default={}, sa_type=JSONB)
    credits_spent: Decimal = Field(default=Decimal('0.0'))
    
    __mapper_args__ = {
        "polymorphic_identity": "model_response",
    }