
def get_id(self):
    return self._id
def get_timestamp(self):
    return self._timestamp

def get_status(self):
    return self._status

def update_status(self, status):
    # pending, processing, completed, failed
    self._status = status
