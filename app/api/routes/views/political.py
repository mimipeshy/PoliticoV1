from flask import request

import app.api.routes.models.political
from app.api.blueprints import version1
from app.api.responses import Responses
from app.api.utils import Validations
from app.api.valid import validate_update_all as v


@version1.route("/party", methods=['GET'])
def get_all_parties():
    """this gets all parties"""
    if not app.api.routes.models.political.parties:
        return Responses.not_found("No created parties yet"), 404
    return Responses.complete_response(app.api.routes.models.political.parties), 200


@version1.route("/party", methods=['POST'])
def create_political_party():
    """this creates a new political party"""
    data = request.get_json()
    empty = Validations.validate_json_inputs()
    if empty:
        return Validations.validate_json_inputs()
    error = Validations.validate_extra_fields(data)
    if error:
        return Validations.validate_extra_fields(data)
    validate = Validations.validate_strings(data)
    if validate:
        return Validations.validate_strings(data)

    # create a party
    if Validations.verify_political_details():
        return Validations.verify_political_details()
    if Validations.validate_characters():
        return Validations.validate_characters()
    if Validations.validate_logo():
        return Validations.validate_logo()
    new_party = {
        'id': len(app.api.routes.models.political.parties) + 1,
        'name': request.json['name'],
        'hqAddress': request.json.get('hqAddress'),
        'logoUrl': request.json.get('logoUrl'),
    }
    app.api.routes.models.political.parties.append(new_party)
    return Responses.created_response(new_party), 201


@version1.route("/party/<int:id>", methods=['GET'])
def get_specific_party(id):
    """this gets a specific party using id"""
    for party in app.api.routes.models.political.parties:
        if id == party['id']:
            return Responses.complete_response(party), 200
    return Responses.not_found("Party not found"), 404


@version1.route("/party/<int:id>/name", methods=['PATCH'])
def update_specific_party(id):
    """this updates a specific party name"""
    validate = v()
    if validate:
        return v()
    res = app.api.routes.models.political.Update.update_party_details(id)
    return res


@version1.route("/party/<int:id>", methods=['DELETE'])
def delete_specific_party(id):
    """this deletes a specific party"""
    for party in app.api.routes.models.political.parties:
        if party["id"] == int(id):
            app.api.routes.models.political.parties.remove(party)
            return Responses.complete_response("Party deleted successfully"), 200
    return Responses.not_found("Party does not exist"), 404
