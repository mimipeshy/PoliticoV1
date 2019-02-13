from app.api.responses import Responses

offices = []


class GovernmentOffice:
    """this initializes political office class methods"""

    def __init__(self, name, type):
        self.id = len(offices) + 1
        self.name = name
        self.type = type

    def add_political_office(self):
        """this saves political party data"""
        new_office = {
            "id": len(offices) + 1,
            "name": self.name,
            "type": self.type

        }
        return new_office

    @staticmethod
    def get_one_office(id):
        data = [offices for office in offices if office["id"] == id]
        if not data:
            return Responses.not_found("Political office not found"), 404
        return Responses.complete_response(data)

    @staticmethod
    def get_all_offices():
        return Responses.complete_response(offices)
