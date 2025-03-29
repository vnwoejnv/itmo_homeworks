from typing import Dict, List, Tuple, Optional, Any


class User: #супер класс для пользователя и администратора
    def __init__(self, username: str, email: str, password: str):
        self.__username = username
        self.__email = email 
        self.__password_hash = self._hash_password(password)
        self.__id = None  # Будет назначен при сохранении в БД
    
    def _hash_password(self, password: str) -> str:
        pass

    #геттеры и сеттеры...

   

class RegularUser(User):
    def __init__(self, username: str, email: str, password: str):
        super().__init__(username, email, password)
        self.__balance = 0.0
        self.__prediction_history = []
        self.__transaction_history = []

    def make_prediction_request(self, data: Dict[str, Any]):
        #как-то обратиться к классу ModelRequest и сделать запрос
        pass
        
    def balance_deposit_request(self, amount: float) -> bool:
        #как-то обратиться к классу TransactionRequest и пополнить баланс
        pass

    def watch_requests_history(self):
        #обратитьсяк классу RequestsHistorySearch и увидеть свои запросы к модели
        pass

    def watch_transactions_history(self):
        # обратиться к классу TransactionsHistorysearch и увидеть свои пополнения
        pass

    


class adminUser(User):
    def __init__(self, username: str, email: str, password: str):
        super().__init__(username, email, password)
        
    def add_balance_to_user(self, user_id: int, amount:float) -> bool:
        # через TransactionService (наверно)
        pass

    def watch_user_transactions_history(self, user_id) -> list: # все через класс TransactionsHistorySearch
        pass
    
    def watch_pending_transactions(self) -> list:
        pass


    def view_all_transactions(self) -> list:
        pass