# from api.services.q1 import Query1API

from services.q1 import Query1API
from services.q2 import Query2API
from services.q3 import  Query3API
from services.q4 import  Query4API
from services.q5 import  Query5API

from flask import Blueprint

query_api = Blueprint('queryapi', __name__)

query_api.add_url_rule("/q1", view_func=Query1API.as_view("Get division wise total sales"))
query_api.add_url_rule("/q2", view_func=Query2API.as_view("Get transaction(cash/mobile/card) wise total saless"))
query_api.add_url_rule("/q3", view_func=Query3API.as_view("Get Total sales in Barisal"))
query_api.add_url_rule("/q4", view_func=Query4API.as_view("Get Total sales in 2015"))
query_api.add_url_rule("/q5", view_func=Query5API.as_view("Get Total sales in Barisal at 2015"))