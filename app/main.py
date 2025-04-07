from database.config import get_settings
#from database.database import get_session, init_db, get_database_engine
# from services.crud.user import get_all_users, create_user
# from sqlmodel import Session
# from models.event import Event
# from models.user import User


if __name__ == "__main__":
    settings = get_settings()
    print(settings.APP_NAME)
    print(settings.API_VERSION)
    print(f'Debug: {settings.DEBUG}')
    
    print(settings.DB_HOST)
    print(settings.DB_NAME)
    print(settings.DB_USER)