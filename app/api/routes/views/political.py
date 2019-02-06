from os import abort

from flask import request, jsonify, make_response

from app.api.blueprints import version1
from app.api.routes.models.political import PoliticalParty as p, parties
from app.api.utils import Validations


@version1.route("/party", methods=['GET'])
def get_all_parties():
    if not parties:
        return make_response(jsonify({"msg": "no created parties"}))
    else:
        res = p.get_all_parties()
        return res


@version1.route("/party", methods=['POST'])
def create_political_party():
    """this creates a new political party"""

    data = request.get_json(force=True)
    party_name = data["party_name"]
    description = data["description"]
    location = data["location"]
    if Validations.verify_political_details(party_name, description, location):
        return jsonify({"Message": "Missing field/s, fill in the details"})
    product = p(party_name, description, location)
    product.add_political_party()
    return make_response(jsonify({
        "Status": "OK",
        "Message": "Party created successfully",
        "Party Details": parties

    }), 201)


@version1.route("/party/<int:party_id>", methods=['GET'])
def get_specific_party(party_id):
    for party in parties:
        if party_id == party['party_id']:
            return jsonify({'party details': party})
    return make_response(jsonify({"msg": "Party not found"}),404)


@version1.route("/party/<int:party_id>", methods=['PUT'])
def update_specific_party(party_id):
    data = request.get_json()
    res = p(data['party_name'], data['description'], data['location']).update_party_details(party_id)
    return res


@version1.route("/party/<int:party_id>", methods=['DELETE'])
def delete_specific_party(party_id):
    data = [parties for party in parties if party["party_id"] == party_id]
    if not data:
        return make_response(jsonify({
            "status": "OK",
            "Product": "Political party not found"
        }), 404)
    parties.remove(parties[0])
    return make_response(jsonify({
        "status": "OK",
        "Message": "Party deleted"
        }), 200)