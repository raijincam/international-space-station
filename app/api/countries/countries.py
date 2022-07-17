from . import country, country_schema
from flask import (make_response, abort)

def read_all():
    countries = country.query.all()
    countries_schema = country_schema(many=True)
    return countries_schema.dump(countries).data