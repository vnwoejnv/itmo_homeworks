#тк пользователь может выполнить как запрос для пололнения баланса, так и запрос к модели
#удобно описать некотоыре общие свойства запроса тут 
from datetime import datetime

class RequestTracker:
    def __init__(self):
        self._id = None
        self._timestamp = datetime.now()
        self._status = 'pending'

    def get_id(self):
        return self._id

    def get_timestamp(self):
        return self._timestamp
    
    def get_status(self):
        return self._status
    
    def update_status(self, status):
        # pending, processing, completed, failed
        self._status = status



class OperationResult:
    def __init__(self, request_id: int):
        self._id = None
        self._request_id = request_id
        self._completion_time = datetime.now()
    
    def get_id(self):
        return self._id
        
    def get_request_id(self):
        return self._request_id
        
    def get_completion_time(self):
        return self._completion_time