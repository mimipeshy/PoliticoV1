from flask import make_response, jsonify, request

parties = []


class PoliticalParty:
    """this initializes political party class methods"""
    """" Initialize a product description"""

    def __init__(self, party_name, description, location):
        self.party_id = len(parties) + 1
        self.party_name = party_name
        self.location = location
        self.description = description

    @staticmethod
    def add_political_party(party_name, description, location):
        """this saves political party data"""
        new_party = {
            "party_id": len(parties) + 1,
            "party_name": party_name,
            "description": description,
            "location": location
        }
        parties.append(new_party)

    @staticmethod
    def get_all_parties():
        return make_response(jsonify(
            {
                "status": "OK",
                "Message": "These are all political parties",
                "Political Party": parties
            }))


    @staticmethod
    def update_party_details(party_id):
        task = [party for party in parties if party["party_id"] == party_id]
        if not task:
            return make_response(jsonify({
                "status": "OK",
                "Message": "party not found"
            }), 404)

        task[0]['description'] = request.json.get('description', task[0]['description'])
        task[0]['location'] = request.json.get('location', task[0]['location'])
        task[0]['party_name'] = request.json.get('party_name', task[0]['party_name'])
        return make_response(jsonify({
            "status": "OK",
            "Message": "Updated",
            "new details": task[0]
        }), 200)

