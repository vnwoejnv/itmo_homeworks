from models.user import User, RegularUser#, AdminUser
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from typing import List, Optional

def create_regular_user(user: RegularUser, session: Session) -> RegularUser:
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        session.rollback()
        raise

def get_all_regular_users(session: Session) -> List[RegularUser]: #пока что без запросов 
    try:
        statement = select(RegularUser).options(
                    selectinload(RegularUser.model_requests),
                    selectinload(RegularUser.transaction_requests)
                    )
        users = session.exec(statement).all()
        return users
    except Exception as e:
        session.rollback()
        raise

def get_regular_user_by_name(user_name: str, session: Session) -> Optional[RegularUser]:
    try:
        statement = select(RegularUser).where(RegularUser.username == user_name)
        user = session.exec(statement).first()
        return user
    except Exception as e:
        session.rollback()
        raise

def get_regular_user_by_email(email: str, session: Session) -> Optional[RegularUser]:
    try:
        statement = select(RegularUser).where(RegularUser.email == email)
        user = session.exec(statement).first()
        return user
    except Exception as e:
        session.rollback()
        raise

def delete_regular_user_by_name(user_name, session: Session) -> bool:
    try:
        user = get_regular_user_by_name(user_name, session)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise   





#admin
# def create_admin_user(user: User, session: Session) -> AdminUser:
#     try:
#         session.add(user)
#         session.commit()
#         session.refresh(user)
#         return user
#     except Exception as e:
#         session.rollback()
#         raise

# def get_admin_user_by_name(user_name: str, session: Session) -> Optional[AdminUser]:
#     """
#     Get user by ID.
    
#     Args:
#         user_id: User ID to find
#         session: Database session
    
#     Returns:
#         Optional[User]: Found user or None
#     """
#     try:
#         statement = select(AdminUser).where(AdminUser.username == user_name)
#         user = session.exec(statement).first()
#         return user
#     except Exception as e:
#         session.rollback()
#         raise

# def delete_admin_user_by_name(user_name, session: Session) -> bool:
#     try:
#         user = get_admin_user_by_name(user_name, session)
#         if user:
#             session.delete(user)
#             session.commit()
#             return True
#         return False
#     except Exception as e:
#         session.rollback()
#         raise 
