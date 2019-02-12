from flask import jsonify, make_response, request
from app.api.responses import Responses

from app.api.blueprints import version1
from app.api.routes.models.office import GovernmentOffice as q, office


@version1.route("/office", methods=['POST'])
def create_an_office():
    """this creates a new office"""
    data = request.get_json()
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