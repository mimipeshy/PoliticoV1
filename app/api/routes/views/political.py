from flask import request, jsonify, make_response

from app.api.blueprints import version1
from app.api.routes.models.political import PoliticalParty as p, party
from app.api.utils import Validations


@version1.route("/party", methods=['POST'])
def create_political_party():
    """this creates a new political party"""
    data = request.get_json(force=True)
    party_name = data["party_name"]
    description = data["description"]
    location = data["location"]
    if Validations.verify_political_details(party_name, description, location):
        return jsonify({"msg": "fill in the details"})
    else:
        res = p.add_political_party(party_name, description, location)
        return make_response(jsonify({
            "party": res
        }), 201)


@version1.route("/party", methods=['GET'])
def get_all_parties():
    if len(party) < 1:
        return make_response(jsonify({"msg": "no created parties"}))
    else:
        res = p.get_all_parties()
        return res


@version1.route("/party/<int:party_id>", methods=['GET'])
def get_specific_party(party_id):
    res = p.get_one_party(party_id)
    return res


@version1.route("/party/<int:party_id>", methods=['PUT'])
def update_specific_party(party_id):
    data = request.get_json()
    res = p(data['party_name'], data['description'], data['location']).update_party_details(party_id)
    return res


@version1.route("/party/<int:party_id>", methods=['DELETE'])
def delete_specific_party(party_id):
    res = p.delete_one_party(party_id)
    return res