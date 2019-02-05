from flask import jsonify, make_response, request

from app.api.blueprints import version1
from app.api.routes.models.office import GovernmentOffice as q, office


@version1.route("/office", methods=['POST'])
def create_an_office():
    data = request.get_json()
    final = q(data['office_name'], data['description'], data['location']).add_political_office()
    # add to a list and return it
    office.append(final)
    return make_response(jsonify({
        "party": office
    }), 201)


@version1.route("/office/<int:office_id>", methods=['GET'])
def get_one_office(office_id):
    res = q.get_one_office(office_id)
    return res


@version1.route("/office", methods=['GET'])
def get_all_offices():
    if len(office) < 1:
        return make_response(jsonify({"msg": "no created offices"}))
    else:
        res = q.get_all_offices()
        return res
