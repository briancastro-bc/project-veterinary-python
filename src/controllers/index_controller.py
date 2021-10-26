from flask import request
from flask.views import MethodView

class IndexController(MethodView):

    def __init__(self) -> None:
        super().__init__()
    
    def get(self):
        return "Hello World!"