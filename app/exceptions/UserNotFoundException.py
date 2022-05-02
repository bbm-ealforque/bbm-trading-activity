class UserNotFoundException(Exception):
    
    def __init__(self, message=""):
        super().__init__(message)
        self.message = message

    def get_response(self):
        return self.message

    def get_status(self):
        return 404