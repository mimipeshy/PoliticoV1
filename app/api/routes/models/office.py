from flask import make_response, jsonify

office = []


class GovernmentOffice:
    """this initializes political office class methods"""

    def __init__(self, office_name,type):
        self.office_id = len(office) + 1
        self.office_name = office_name
        self.type = type


    def add_political_office(self):
        """this saves political party data"""
        new_office = {
            "office_id": len(office) + 1,
            "office_name": self.office_name,
            "type": self.type

        }
        return new_office

    @staticmethod
    def get_one_office(office_id):
        data = [offices for offices in office if offices["office_id"] == office_id]
        if not data:
            return make_response(jsonify({
                "status": "OK",
                "Product": "Political office not found"
            }), 404)
        return make_response(jsonify({
            "status": "OK",
            "product": data
        }), 200)

    @staticmethod
    def get_all_offices():
        return make_response(jsonify(
            {"status": "OK",
             "Message": "These are all political offices",
             "Political office": office
             }))