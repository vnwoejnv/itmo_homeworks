

from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any
from CompositionUtils import RequestTracker, OperationResult

class ModelRequest: # отвечает за хранение данных запроса
    def __init__(self, userId: int, data: Dict[str, Any]):
        self._tracker = RequestTracker() # id, timestamp, status (используем композицию)
        self._userId = userId
        self._input_data = data
 
    # как я понял пока не нужна реализация (но не удалять же их!)
    # def get_user_id(self) -> int:
    #     return self._user_id
        
    # def get_input_data(self) -> Dict[str, Any]:
    #     return self._input_data
        
        
   



class ModelResponce(): # отвечает за хранение данных ответа
  def __init__(self, request_id: int, valid_data, invalid_data, result, credits_spent):
     self._base = OperationResult(request_id)
    #  self._id = None
    #  self._request_id = request_id
    #  self._completion_time = datetime.now()
     
     self._result = result
     self._credits_spent = credits_spent
     


class MLService():
  def validate_data(input_data):
    valid_data = {}
    invalid_data = {}
    return valid_data, invalid_data
  
  @staticmethod
  def predict(valid_data):
    result = {}
    # уже как-то работает непосредственно с Model
    return result 
  
  @staticmethod
  def calculate_credits(valid_data) -> float:
     cost = 1.0
     return cost
  
  @staticmethod
  def process_peridiction_request(request: ModelRequest) -> ModelResponce:
    # взять данные из запроса (когда будут геттеры), провести валидацию, запихать в модель и вернуть ответ ModelResponce и стоимость 
    pass




  class Model:
    def __init__(self, name: str, version: str = "1.0", **kwargs):
        self._name = name
        self._version = version
        self._options = kwargs
    
    def predict(self, data: dict) -> dict: # для predict в MLService
        result = {} 
        return result
    
    # def get_name(self) -> str:
    #     return self._name
        
    # def get_version(self) -> str:
    #     return self._version