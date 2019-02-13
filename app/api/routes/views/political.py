import re
from os import abort

from flask import request, make_response, jsonify

from app.api.blueprints import version1
from app.api.routes.models.political import PoliticalParty as p, parties, Update as u
from app.api.utils import Validations
from app.api.responses import Responses


@version1.route("/party", methods=['GET'])
def get_all_parties():
    """this gets all parties"""
    if not parties:
        return Responses.not_found("No created parties yet"), 404
    return Responses.complete_response(parties), 200


@version1.route("/party", methods=['POST'])
def create_political_party():
    """this creates a new political party"""
    data = request.get_json(force=True)
    name = data["name"]
    hqAddress = data['hqAddress']
    logoUrl = data["logoUrl"]

    if Validations.verify_political_details(name, hqAddress, logoUrl):
        return Validations.verify_political_details(name, hqAddress, logoUrl)
    new = p(name, hqAddress, logoUrl)
    new.add_political_party()
    return Responses.created_response(parties), 201


@version1.route("/party/<int:id>", methods=['GET'])
def get_specific_party(id):
    """this gets a specific party using id"""
    for party in parties:
        if id == party['id']:
            return Responses.complete_response(party), 200
    return Responses.not_found("Party not found"), 404


@version1.route("/party/<int:id>/name", methods=['PATCH'])
def update_specific_party(id):
    """this updates a specific party name"""
    res = u.update_party_details(id)
    return res


@version1.route("/party/<int:id>", methods=['DELETE'])
def delete_specific_party(id):
    """this deletes a specific party"""

    for party in parties:
        if party["id"] == int(id):
            parties.remove(party)
            return Responses.complete_response("Party deleted successfully"), 200
    return Responses.not_found("Party does not exist"), 404
