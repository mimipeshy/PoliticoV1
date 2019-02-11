from flask import make_response, jsonify, request

parties = []


class PoliticalParty:
    """this initializes political party class methods"""

    def __init__(self, party_name, logoUrl):
        self.party_id = len(parties) + 1
        self.party_name = party_name
        self.logoUrl = logoUrl

    def add_political_party(self):
        """this saves political party data"""
        new_party = {
            "party_id": len(parties) + 1,
            "party_name": self.party_name,
            "logoUrl": self.logoUrl
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

        task[0]['party_name'] = request.json.get('party_name', task[0]['party_name'])
        task[0]['logoUrl'] = request.json.get('logoUrl', task[0]['logoUrl'])
        return make_response(jsonify({
            "status": "OK",
            "Message": "Updated Party Name",
            "new details": task[0]
        }), 200)