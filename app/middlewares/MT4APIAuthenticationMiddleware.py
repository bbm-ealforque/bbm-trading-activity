from configparser import ConfigParser
from masonite.middleware import Middleware


class MT4APIAuthenticationMiddleware(Middleware):
    """Middleware to check if API is authenticated for MT4 endpoints"""

    def before(self, request, response):
        if not request.header('username') and not request.header('password'):
            return response.view({
                "error": "Access denied",
                "message": "API credential(s) required"
            }, status = 403)

        uname = str(request.header('username'))
        pword = request.header('password')

        conf = ConfigParser()
        conf.read('config.ini')


        if not conf.has_section('mt4-credentials'):
            return response.view({
                "error": "Internal server error",
                "message": "Config file incorrect"
            }, status = 500)

        if not conf.has_option('mt4-credentials', uname):
            return response.view({
                "error": "Access denied",
                "message": "API credential(s) invalid"
            }, status = 403)

        if conf['mt4-credentials'][uname] != pword:
            return response.view({
                "error": "Access denied",
                "message": "API credential(s) invalid"
            }, status = 403)
            
        return request
        

    def after(self, request, response):
        return request
