from masonite.middleware import Middleware
from masonite.middleware.route import CorsMiddleware

class CorsMiddleware(CorsMiddleware):

  headers = {
    'Access-Control-Allow-Origin': "*",
    "Access-Control-Allow-Methods": "DELETE, GET, HEAD, OPTIONS, PATCH, POST, PUT",
    "Access-Control-Allow-Headers": "Content-Type, Accept, X-Requested-With",
    "Access-Control-Max-Age": "3600",
    "Access-Control-Allow-Credentials": "true"
  }