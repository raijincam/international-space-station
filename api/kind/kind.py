from . import type_ship, type_ship_schema
from flask import (make_response, abort)

def read_all():
    kinds = type_ship.query.all()
    kind_schema = type_ship_schema
    return