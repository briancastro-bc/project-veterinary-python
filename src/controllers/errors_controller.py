from flask import render_template
from flask.views import MethodView

class NotFoundController(MethodView):

    def __init__(self) -> None:
        super().__init__()

    def get(self, error):
        return "Not found"