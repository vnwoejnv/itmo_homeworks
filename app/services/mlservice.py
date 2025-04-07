class MLService():
  @staticmethod
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