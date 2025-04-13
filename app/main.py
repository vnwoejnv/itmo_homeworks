from models.user import RegularUser#, AdminUser
from models.requests import ModelRequest, TransactionRequest
from models.responses import ModelResult, TransactionResult

from sqlmodel import SQLModel
from database.config import get_settings
from database.database import get_session, init_db, get_database_engine, engine
from sqlmodel import Session
import services.crud.user as crud_user
import services.crud.request as crud_request

if __name__ == "__main__":
    settings = get_settings()
    print(settings.APP_NAME)
    print(settings.API_VERSION)
    print(f'Debug: {settings.DEBUG}')
    
    print(settings.DB_HOST)
    print(settings.DB_NAME)
    print(settings.DB_USER)

    init_db(drop_all=True)
    print('db successfully created')
    print('--'*20)
    user1 = RegularUser(email='first@gmail', password_hash='111111', username='first')
    user2 = RegularUser(email='second@gmail', password_hash='222222', username='second')
    request1 = ModelRequest(input_data="prompt here")
    request2 = ModelRequest(input_data="prompt here2")
    result1 = ModelResult(output_data="answer")
    result2 = ModelResult(output_data="answer2")
    request1.response = result1
    request2.response = result2
    
    user1.model_requests = [request1]
    user1.model_requests.append(request2)

    with Session(engine) as session:
        # Создаем пользователя
        user1 = crud_user.create_regular_user(user1, session)
        user2 = crud_user.create_regular_user(user2, session)

        user = crud_user.get_regular_user_by_name('first', session)
        print(f'first user email{user.email}')
        users = crud_user.get_all_regular_users(session)
        for request in user.model_requests:
            print(request.input_data)
        print('--'*20)
        
        print('all users:')
        for user in users:
            print(user)
        print('--'*20)

        print('all requests:')
        requests = crud_request.get_all_model_requests(session)
        for req in requests:
            print(req.input_data)
        print('--'*20)
        crud_user.delete_regular_user_by_name(user.username, session)
        print('all done')

        #regular_user = create_regular_user(regular_user, session)


    

