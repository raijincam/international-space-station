from . import combustibles, combustibles_schema
from flask import (make_response, abort)

def read_all():
    combustible = combustibles.query.all()
    combustible_schema = combustibles_schema(many=True)
    return combustible_schema.dump(combustible).data