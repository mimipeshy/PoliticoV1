from flask import make_response, jsonify, request

party = []


class PoliticalParty:
    """this initializes political party class methods"""
    """" Initialize a product description"""

    def __init__(self, party_name, description, location):
        self.party_id = len(party) + 1
        self.party_name = party_name
        self.location = location
        self.description = description

    @staticmethod
    def add_political_party(party_name, description, location):
        """this saves political party data"""
        new_party = {
            "party_id": len(party) + 1,
            "party_name": party_name,
            "description": description,
            "location": location
        }
        party.append(new_party)

    @staticmethod
    def get_all_parties():
        return make_response(jsonify(
            {
                "status": "OK",
                "Message": "These are all political parties",
                "Political Party": party
            }))
