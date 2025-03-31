class HistorySearches:
    def __init__(self, db_connection):
        self._db = db_connection


class TransactionsHistorySearch(HistorySearches):
    def __init__(self, db_connection):
        super().__init__(db_connection)
    
    def find_by_transaction_id(self, transaction_id: int): # просто найти транзакцию
        pass

        
    def find_by_user_id(self, **kwargs): #все транзакции пользователя
       pass
        
    
    def find_pending_transactions(**kwargs): #Находит все транзакции, ожидающие подтверждения (для администратора).
        pass
        

class RequestsHistorySearch:
    def __init__(self, db_connection):
        super().__init__(db_connection)

    def find_by_request_id(self, request_id):
        pass

    def find_by_user_id(self, **kwargs):
        pass

    