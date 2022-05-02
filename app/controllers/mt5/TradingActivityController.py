from app.dto.TradingActivityListDTO import TradingActivityListDTO
from app.dto.UserTradingActivityListDTO import UserTradingActivityListDTO
from http import HTTPStatus
from masonite.controllers import Controller
from masonite.response import Response
from masonite.request import Request

from app.services.mt5.MT5TradingActivityService import MT5TradingActivityService

class TradingActivityController(Controller):
   
    def __init__(self, 
                 request: Request, 
                 service: MT5TradingActivityService):
        self.request = request
        self.service = service

    def index(self, response: Response):
        dto = TradingActivityListDTO(self.request)
        result = self.service.getTradingActivityList(dto)

        return response.json(
            result.serialize(), 
            HTTPStatus.OK
        )

    def indexForUser(self, response: Response):
        dto = UserTradingActivityListDTO(self.request)
        result = self.service.getTradingActivityListForUser(dto)

        return response.json(
            result.serialize(), 
            HTTPStatus.OK
        )
