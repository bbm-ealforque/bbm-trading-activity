from masonite.routes import Route

ROUTES = [
  Route.get("/mt4/users/", "mt4/UserController@index").middleware('auth.api.mt4'),
  Route.get("/mt4/users/@user", "mt4/UserController@show").middleware('auth.api.mt4'),
  Route.get("/mt4/users/@user/trading-activities", "mt4/TradingActivityController@indexForUser").middleware('auth.api.mt4'),
  Route.get("/mt4/trading-activities", "mt4/TradingActivityController@index").middleware('auth.api.mt4'),


  Route.get("/mt5/users/", "mt5/UserController@index").middleware('auth.api.mt5'),
  Route.get("/mt5/users/@user", "mt5/UserController@show").middleware('auth.api.mt5'),
  Route.get("/mt5/users/@user/trading-activities", "mt5/TradingActivityController@indexForUser").middleware('auth.api.mt5'),
  Route.get("/mt5/trading-activities", "mt5/TradingActivityController@index").middleware('auth.api.mt5'),
]
