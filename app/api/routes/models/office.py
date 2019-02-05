from flask import make_response, jsonify

office = []


class PoliticalOffice:
    """this initializes political office class methods"""

    def __init__(self, office_name, description, location):
        self.office_id = len(office) + 1
        self.office_name = office_name
        self.location = location
        self.description = description

    def add_political_office(self):
        """this saves political party data"""
        new_office = {
            "office_id": len(office) + 1,
            "office_name": self.office_name,
            "description": self.description,
            "location": self.location
        }
        return new_office

    