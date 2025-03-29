import User
#мне кажется что этот класс не очень нужен конкретно в этом задании
class AuthService:
    @staticmethod
    def register(username, email, password) -> User:
        new_user = User(username, email, password)
        # Создание нового пользователя (если пройдет проверки логина пароля) и сохранение его в бд
        return new_user
    
    @staticmethod
    def login(username, password):
        # Логика входа
        pass
