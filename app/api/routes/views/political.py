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
