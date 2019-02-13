from flask import request

from app.api.responses import Responses
from app.api.routes.models.office import offices


def validate_update_all():
    data = request.get_json()

    required_fields = ['name']
    if not data:
        return Responses.bad_request("Empty inputs in Json"), 400
    if 'name' not in data:
        return Responses.bad_request("Name input is missing"), 400
    if len(required_fields) < len(data.keys()):
        for key in data:
            if key not in required_fields:
                return Responses.bad_request("{} is not a valid key".format(key)), 400
    if not isinstance(data['name'], str):
        return Responses.bad_request('Ensure that all inputs are strings'), 400
    name = data['name'].strip()
    if len(name) == 0:
        return Responses.bad_request("Party Name cannot be empty"), 400
    if len(name) < 6:
        return Responses.bad_request("Name should have more than 6 characters"), 404
    if not isinstance(data['name'], str):
        return Responses.bad_request('Ensure that all name input is a string'), 400
    for office in offices:
        if office["name"] == name:
            return Responses.bad_request("Office with that name already exists")
