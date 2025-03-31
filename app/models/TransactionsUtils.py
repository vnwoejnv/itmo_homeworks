from CompositionUtils import RequestTracker, OperationResult


# тут все очень похоже на запросы к модели - 2 класса хранят данные запроса и результата
# статический класс реализует логику обработки запроса
class TransactionRequest:
    def __init__(self, user_id, amount, transaction_type):
        self._tracker = RequestTracker()
        self._user_id = user_id
        self._amount  = amount
        self._type = transaction_type # 'deposit', 'withdrawal'

    # геттеры сеттеры
    def get_id(self):
        return self._tracker.get_id()
        
    def get_status(self):
        return self._tracker.get_status()
    # и другие

class TransactionResult:
    def __init__(self, request_id: int, approved: bool, admin_id: int = None, notes: str = None):
        self._base = OperationResult(request_id) #
        # self._id = None 
        # self._request_id = request_id
        # self.completion_time = datetime.now()
        
        self._approved = approved
        self._admin_id = admin_id
        self._notes = notes
        


class TransactionService:
    """Обрабатывает запрос на пополнение баланса"""
    #тут все сложно, надо обработать запрос пользователя либо если админ явно пополняет кому-то баланс либо если он просто одобряет пополнение
    pass
    