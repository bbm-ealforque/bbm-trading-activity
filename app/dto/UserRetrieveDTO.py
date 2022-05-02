from masonite.request import Request

class UserRetrieveDTO:

    def __init__(self, 
                 request: Request):
        self.request = request
        self.userId = request.param('user')
        self.loggedUser = request.header('username')

    def getUserId(self):
        return self.userId

    def getLoggedUser(self):
        return self.loggedUser