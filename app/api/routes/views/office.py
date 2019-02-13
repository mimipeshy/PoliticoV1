from flask import jsonify, make_response, request
from app.api.responses import Responses

from app.api.blueprints import version1
from app.api.routes.models.office import GovernmentOffice as q, office

@version1.route("/office", methods=['POST'])
def create_an_office():
    """this creates a new office"""
    data = request.get_json()
    required_fields = ['name', 'type']
    if not data:
        return Responses.bad_request("Empty inputs in Json"), 400
    if 'name' not in data:
        return Responses.bad_request("Name input is missing"), 400
    if 'type' not in data:
        return Responses.bad_request("Type input is missing"), 400
    if len(required_fields) < len(data.keys()):
        for key in data:
            if key not in required_fields:
                return Responses.bad_request("{} is not a valid key".format(key)), 400
    if not isinstance(data['name'], str) or not isinstance(data['type'], str):
        return Responses.bad_request('Ensure that all inputs are strings'), 400
    name = data['name'].strip()
    type = data['type'].strip()
    if len(name) == 0:
        return Responses.bad_request("Office Name cannot be empty"), 400
    if len(type) == 0:
        return Responses.bad_request("Type cannot be empty"), 400
    if len(name) < 6:
        return Responses.bad_request("Office Name should have more than 6 characters"), 404
    final = q(data["name"], data["type"]).add_political_office()
    # add to a list and return it
    office.append(final)
    return Responses.created_response(office), 201


@version1.route("/office/<int:id>", methods=['GET'])
def get_one_office(id):
    """this gets one specific office"""
    res = q.get_one_office(id)
    return res


@version1.route("/office", methods=['GET'])
def get_all_offices():
    """this returns all offices"""
    if len(office) < 1:
        return Responses.not_found("No created offices"), 404
    else:
        res = q.get_all_offices()
        return res