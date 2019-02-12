from flask import request

from app.api.responses import Responses

parties = []


class PoliticalParty:
    """this initializes political party class methods"""

    def __init__(self, name, hqAddress, logoUrl):
        self.party_id = len(parties) + 1
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    def add_political_party(self):
        """this saves political party data"""
        new_party = {
            "id": len(parties) + 1,
            "name": self.name,
            "hqAddress": self.hqAddress,
            "logoUrl": self.logoUrl
        }
        parties.append(new_party)

    @staticmethod
    def get_all_parties():
        return Responses.complete_response(parties)

    @staticmethod
    def update_party_details(id):
        task = [party for party in parties if party["id"] == id]
        if not task:
            return Responses.not_found("Party not found"), 404
        task[0]['name'] = request.json.get('name', task[0]['name'])
        task[0]['logoUrl'] = request.json.get('logoUrl', task[0]['logoUrl'])
        return Responses.complete_response(task[0])