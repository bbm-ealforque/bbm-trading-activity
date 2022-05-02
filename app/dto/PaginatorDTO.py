from masonite.request import Request

class PaginatorDTO:

    def __init__(self, 
                 request: Request):
        self.page = request.input("page", "1")
        self.perPage = request.input("perPage", "10")

    def getPage(self):
        return int(self.page)

    def getPerPage(self):
        return int(self.perPage)