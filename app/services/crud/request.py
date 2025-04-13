from models.user import RegularUser#, AdminUser
from models.requests import ModelRequest, TransactionRequest
from sqlmodel import Session, select
from typing import List, Optional

def get_all_model_requests(session) -> List[ModelRequest]: #добавить результат
    try:
        statement = select(ModelRequest)
        requests = session.exec(statement).all()
        return requests
    except Exception as e:
        raise

def get_model_request_by_id(request_id: int, session: Session) -> Optional[ModelRequest]:
    try:
        statement = select(ModelRequest).where(ModelRequest.id == request_id)
        request = session.exec(statement).first()
        return request
    except Exception as e:
        session.rollback()
        raise


def create_model_request(request: ModelRequest, session: Session) -> ModelRequest:
    try:
        session.add(request)
        session.commit()
        session.refresh(request)
        return request
    except Exception as e:
        session.rollback()
        raise

def delete_model_request(request_id: int, session: Session) -> bool:
    try:
        request = get_model_request_by_id(request_id, session)
        if request:
            session.delete(request)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise


