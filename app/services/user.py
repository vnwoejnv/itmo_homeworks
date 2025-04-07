def make_prediction_request(self, data: Dict[str, Any]):
    
    pass
    
def balance_deposit_request(self, amount: float) -> bool:
    
    pass
def watch_requests_history(self):
    #обратитьсяк классу RequestsHistorySearch и увидеть свои запросы к модели
    pass
def watch_transactions_history(self):
    # обратиться к классу TransactionsHistorysearch и увидеть свои пополнения
    pass



# для администратора 
def add_balance_to_user(self, user_id: int, amount:float) -> bool:
    pass
def watch_user_transactions_history(self, user_id) -> list: 
    pass

def watch_pending_transactions(self) -> list:
    pass
def view_all_transactions(self) -> list:
    pass